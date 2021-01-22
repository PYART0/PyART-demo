This is the README file for the paper Python API Recommendation in Real-Time.

Access Link
Link1: The dataset, baseline, code and other information for PyART can be obtained at: 
https://github.com/PYART0/PyART

Link2: A quick and execuable testing demo for PyART can be obtained at: 
https://github.com/PYART0/PyART-demo

How to repeat/replicate/reproduce the results in paper

##Operation System:##

 The experiments of PyART are performed on Linux (Ubuntu 18+). The operation system can be downloaded on https://ubuntu.com/download/desktop.

##Evaluation##

The evaluation results of PyART include three aspects, including Task1 (Dataflow evaluation) and Task2 (API recommendation evaluation).

##Task1: Data flow analysis evaluation stored in Table III.## 

The task is stored in DataFlowEvaluation dictionary in Link2.

To run Task1, the following requirements are needed:

Java version >= 11

Python version >= 3.6

To run the baseline Pysonar2 for Task1, use the following command:

java -Xms3550M -jar pystyping-3.0-milestone.jar data/PROJ results/PROJ -clearcache

In which PROJ denotes project names, such as:

java -Xms3550M -jar pystyping-3.0-milestone.jar data/cornice results/cornice -clearcache

or:

chmod a+x runpystyping.sh

./runpystyping.sh

The input is stored in data/ and output is stored in results/. The dataflows are stored in results/PROJ/all-bindings.txt, results/PROJ/all-references.txt 
and results/PROJ/all-constraints.txt.

To run PyART for Task1, use the following command:

python3 main_dataflow.py > results/PROJ.txt

The input is stored in data/ and output is stored in results/PROJ.txt

Since the ground truth of Task1 is obtained manually, the manual results is stored in ManaulCheckResults.xlsx.


How to reproduce Task1 for other projects:

-Store your project in data/ and change PROJ to your project name. Change the root_path variable to your project name in main_dataflow.py in line 39.


##Task2: API recommendation evaluation.##

Task2 is stored in PyART dictionary in Link2, and includes two kinds of evaluation: intra-project recommendation (Table IV and Table V) and across-project recommendation (Table VI ). Each evaluation includes two process: training and testing.

To run Task2, the following requirements are needed:

Python version >= 3.6

apt-get install libnss3 libfontconfig gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget

python3 -m pip install --upgrade pip

python3 -m pip install pytype sklearn pandas joblib nltk

If the terminal outputs errors about punkt of nltk_data, you can download nltk_data from https://github.com/nltk/nltk_data, and unzip punkt.zip in nltk_data/packages/tokenizers/, and run cp -r nltk_data/packages/tokenizers/  nltk_data/

To run training process of intra-project recommendation in Task2, use the following command:

python3 aget_train_kfold.py

The result of the command, which is set of feature vectors and labels, is output to *.csv files in traincsv/ dictionary. The input of the command is stored in testdata/.  Then use the following command to generate RF model:

python3 generateclf.py

The model is stored as *.pkl in traincsv/ dictionary.

To reproduce training for your own project:

Store your project in testdata/, change the CURRENT_PROJ in aget_train_kfold.py in line 1329, and change the proj_name variable in generateclf.py in line 6.

To run testing process of intra-project recommendation in Task2, use the following command:

python3 aget_test_result.py

The recommendation results are printed in real time, you can use python3 aget_test_result.py > FILENAME to store results.

To reproduce testing for your own project:

Store your project in testdata/, change the CURRENT_PROJ in aget_test_result.py in line 1463.

Other information in PyART:

The testJson/ dictionary stores *.json files that collect def information of the target project. Of course, the json file can be obtained directly by Regular Expression Extraction. In our demo, we extract it with understand tool. If you want to use understand, you should download understand for linux and use the following commands:

vim ~/.bashrc

export PATH="$PATH:/[path]/understand/scitools/bin/linux64"

export STIHOME="/[path]/understand/scitools"

export LD_LIBRARY_PATH="/[path]/understand/scitools/bin/linux64"

[This is not necessary if you do not use understand]

To run training process of across-project recommendation in Task2, use the following command:

python3 get_train_kfold.py

The result of the command, which is set of feature vectors and labels, is output to *.csv files in traincsv-1/ dictionary. The input of the command is stored in traindata/. Since the training data for across-project is large, we only put a single project in traindata/, you can get our all training projects from Github with TrainDataList.txt.
Then use the following command to generate RF model:

python3 ac_generateclf.py

The model is stored as total.pkl in traincsv-1/ dictionary.

To run testing process of across-project recommendation in Task2, use the following command:

python3 bget_test_result.py

The recommendation results are printed in real time, you can use python3 bget_test_result.py > FILENAME to store results.

To reproduce testing for your own project:

Store your project in testdata/, change the CURRENT_PROJ in bget_test_result.py in line 1463.

