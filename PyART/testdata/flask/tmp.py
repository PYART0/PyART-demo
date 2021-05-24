from contextlib import contextmanager

import werkzeug.test
from click.testing import CliRunner
from werkzeug.test import Client
from werkzeug.urls import url_parse

from . import _request_ctx_stack
from .cli import ScriptInfo
from .json import dumps as json_dumps


class EnvironBuilder(werkzeug.test.EnvironBuilder):

    def __init__(
        self,
        app,
        path="/",
        base_url=None,
        subdomain=None,
        url_scheme=None,
        *args,
        **kwargs,
    ):
        assert not (base_url or subdomain or url_scheme) or (
            base_url is not None
        ) != bool(
            subdomain or url_scheme
        ), 'Cannot pass "subdomain" or "url_scheme" with "base_url".'

        if base_url is None:
            http_host = app.config.get("SERVER_NAME") or "localhost"
            app_root = app.config["APPLICATION_ROOT"]

            if subdomain:
                http_host = f"{subdomain}.{http_host}"

            if url_scheme is None:
                url_scheme = app.config["PREFERRED_URL_SCHEME"]

            url = url_parse(path)
            base_url = (
                f"{url.scheme or url_scheme}://{url.netloc or http_host}"
                f"/{app_root.lstrip('/')}"
            )
            path = url.path

            if url.query:
                sep = b"?" if isinstance(url.query, bytes) else "?"
                path += sep + url.query

        self.app = app
        super().__init__(path, base_url, *args, **kwargs)

    def json_dumps(self, obj, **kwargs):
        kwargs.setdefault("app", self.app)
        return json_dumps(obj, **kwargs)


class FlaskClient(Client):

    preserve_context = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.environ_base = {
            "REMOTE_ADDR": "127.0.0.1",
            "HTTP_USER_AGENT": f"werkzeug/{werkzeug.__version__}",
        }

    @contextmanager
    def session_transaction(self, *args, **kwargs):
        if self.cookie_jar is None:
            raise RuntimeError(
                "Session transactions only make sense with cookies enabled."
            )
        app = self.application
        environ_overrides = kwargs.setdefault("environ_overrides", {})
        self.cookie_jar.inject_wsgi(environ_overrides)
        outer_reqctx = _request_ctx_stack.top
        with app.test_request_context(*args, **kwargs) as c:
            session_interface = app.session_interface
            sess = session_interface.open_session(app, c.request)
            if sess is None:
                raise RuntimeError(
                    "Session backend did not open a session. Check the configuration"
                )

            _request_ctx_stack.push(outer_reqctx)
            try:
                yield sess
            finally:
                _request_ctx_stack.pop()

            resp = app.response_class()
            if not session_interface.is_null_session(sess):
                session_interface.save_session(app, sess, resp)
            headers = resp.get_wsgi_headers(c.request.environ)
            self.cookie_jar.extract_wsgi(c.request.environ, headers)

    def open(self, *args, **kwargs):
        as_tuple = kwargs.pop("as_tuple", False)
        buffered = kwargs.pop("buffered", False)
        follow_redirects = kwargs.pop("follow_redirects", False)

        if (
            not kwargs
            and len(args) == 1
            and isinstance(args[0], (werkzeug.test.EnvironBuilder, dict))
        ):
            environ = self.environ_base.copy()

            if isinstance(args[0], werkzeug.test.EnvironBuilder):
                environ.update(args[0].get_environ())
            else:
                environ.update(args[0])

            environ["flask._preserve_context"] = self.preserve_context
        else:
            kwargs.setdefault("environ_overrides", {})[
                "flask._preserve_context"
            ] = self.preserve_context
            kwargs.setdefault("environ_base", self.environ_base)
            builder = EnvironBuilder(self.application, *args, **kwargs)

            try:
                environ = builder.get_environ()
            finally:
                builder.close()

        return Client.open(
            self,
            environ,
            as_tuple=as_tuple,
            buffered=buffered,
            follow_redirects=follow_redirects,
        )

    def __enter__(self):
        if self.preserve_context:
            raise RuntimeError("Cannot nest client invocations")
        self.preserve_context = True
        return self

    def __exit__(self, exc_type, exc_value, tb):
        self.preserve_context = False

        while True:
            top = _request_ctx_stack.top

            if top is not None and top.preserved:
                reveal_type(top)