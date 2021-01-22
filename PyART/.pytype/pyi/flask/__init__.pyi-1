
from typing import Any
def __getattr__(name: Any) -> Any: ...
# Caught error in pytype: 'NoneType' object has no attribute 'constants'
# Traceback (most recent call last):
#   File "/usr/local/lib/python3.6/dist-packages/pytype/io.py", line 156, in check_or_generate_pyi
#     input_filename=options.input, options=options, loader=loader)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/io.py", line 113, in generate_pyi
#     analyze.infer_types, input_filename, options, loader)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/io.py", line 65, in wrapper
#     return f(*args, **kwargs)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/io.py", line 84, in _call
#     deep=deep)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/analyze.py", line 656, in infer_types
#     loc, defs = tracer.run_program(src, filename, init_maximum_depth)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 811, in run_program
#     node, f_globals, f_locals, _ = self.run_bytecode(node, code)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 778, in run_bytecode
#     node, return_var = self.run_frame(frame, node)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 373, in run_frame
#     state = self.run_instruction(op, state)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 331, in run_instruction
#     state = bytecode_fn(state, op)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 2836, in byte_IMPORT_FROM
#     state, attr = self.load_attr_noerror(state, module, name)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 1454, in load_attr_noerror
#     node, result, _ = self._retrieve_attr(state.node, obj, attr)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/vm.py", line 1355, in _retrieve_attr
#     node, val.data, attr, val)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/attribute.py", line 57, in get_attribute
#     return self._get_module_attribute(node, obj, name, valself)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/attribute.py", line 196, in _get_module_attribute
#     node, var = self._get_instance_attribute(node, module, name, valself)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/attribute.py", line 225, in _get_instance_attribute
#     return self._get_attribute(node, obj, obj.cls, name, valself)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/attribute.py", line 258, in _get_attribute
#     node, attr = self._get_member(node, obj, name)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/attribute.py", line 392, in _get_member
#     obj.load_lazy_attribute(name)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/abstract.py", line 663, in load_lazy_attribute
#     variable = self._convert_member(name, self._member_map[name])
#   File "/usr/local/lib/python3.6/dist-packages/pytype/abstract.py", line 3638, in _convert_member
#     var = self.vm.convert.constant_to_var(ty)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/convert.py", line 382, in constant_to_var
#     discard_concrete_values)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/convert.py", line 412, in constant_to_var
#     result = self.constant_to_value(pyval, subst, node)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/convert.py", line 465, in constant_to_value
#     value = self._constant_to_value(pyval, subst, get_node)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/convert.py", line 635, in _constant_to_value
#     pyval.function, subst, self.vm.root_cfg_node)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/convert.py", line 465, in constant_to_value
#     value = self._constant_to_value(pyval, subst, get_node)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/convert.py", line 607, in _constant_to_value
#     for sig in pyval.signatures]
#   File "/usr/local/lib/python3.6/dist-packages/pytype/convert.py", line 607, in <listcomp>
#     for sig in pyval.signatures]
#   File "/usr/local/lib/python3.6/dist-packages/pytype/function.py", line 505, in __init__
#     for p in self.pytd_sig.params]
#   File "/usr/local/lib/python3.6/dist-packages/pytype/function.py", line 505, in <listcomp>
#     for p in self.pytd_sig.params]
#   File "/usr/local/lib/python3.6/dist-packages/pytype/convert.py", line 465, in constant_to_value
#     value = self._constant_to_value(pyval, subst, get_node)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/convert.py", line 638, in _constant_to_value
#     for t in pyval.type_list]
#   File "/usr/local/lib/python3.6/dist-packages/pytype/convert.py", line 638, in <listcomp>
#     for t in pyval.type_list]
#   File "/usr/local/lib/python3.6/dist-packages/pytype/convert.py", line 465, in constant_to_value
#     value = self._constant_to_value(pyval, subst, get_node)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/convert.py", line 574, in _constant_to_value
#     return self._create_module(mod)
#   File "/usr/local/lib/python3.6/dist-packages/pytype/convert.py", line 506, in _create_module
#     ast.functions + ast.aliases)
# AttributeError: 'NoneType' object has no attribute 'constants'