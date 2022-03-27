# Software_Cost_Estimation
| Details                   |                                             |
|---------------------------|---------------------------------------------|
| Programming Language:     |  Python 3.**6**                             |
| sklearn                   |  0.23.2                                     |
| Models Required:          | model1(maxwell.joblib)                      |
|                           | model2(desharnais.joblib)                   |
|                           | model3(maxwell_without_kmean_leaners.joblib)|
|                           | model4(desh_without_kmean_leaners.joblib)   |



#Short introduction to the project
This is a project that helps estimate the cost of a project considering certain features.

## Project Set Up and Installation
*TODO:* Explain the setup procedures to run your project. For instance, this can include your project directory structure, the models you need to download and where to place them etc. Also include details about how to install the dependencies your project requires.

[step 1]
The project heavily depends on python as it's the language used to run the whole program so, the first thing to do is to install python before proceeding.

[step 2]
install pip, pip is a python package that helps install other python packages.

[step 3]
use pip to install the rest of the required package. To do this, make sure your current directory structure looks like this from the terminal or command line.
.
├── dataset
│   |── desh_X_test_sca.csv
|   |── desh_X_train_sca.csv
|   |── desh_y_test.csv
|   |── desh_y_train.csv
|   |── maxwell_X_test_sca.csv
|   |── maxwell_X_train_sca.csv
|   |── maxwell_y_test.csv
|   └── maxwell_y_train.csv
|
├── saved_models
│   |── desh_data_pipeline.joblib
|   |── desh_leaners.joblib
|   |── desh_scaler.joblib
|   |── desh_without_kmean_leaners.joblib
|   |── maxwell_data_pipeline.joblib
|   |── maxwell_leaners.joblib
|   |── maxwell_scaler.joblib
|   └── maxwell_without_kmean_leaners.joblib
|
|── __init__.py
|── .gitignore
|── process_data.py
├── README.md
├── requirements.txt
|── test.py
|── train.py
|── WRITEUP.md
|── model.py

type, 
pip install -r requirements.txt 

this command will install other required package for the project.

#model
This project also depends on just eight(8) models, to run which is the result of the training of a pretrained algorithms, The models are (desh_data_pipeline.jobli, desh_leaners.joblib, desh_scaler.joblib, desh_without_kmean_leaners.joblib, maxwell_data_pipeline.joblib, maxwell_leaners.joblib, maxwell_scaler.joblib, maxwell_without_kmean_leaners.joblib). This models will be together with the file. In Addition, eight(8) dataset files in csv format willl be required to completed run default train and test, these files are (desh_X_test_sca.csv, desh_X_train_sca.csv, desh_y_test.csv, desh_y_train.csv, maxwell_X_test_sca.csv, maxwell_X_train_sca.csv, maxwell_y_test.csv, maxwell_y_train.csv).

#how to use the process_data.py script

#demo run process_data.py
use the python3 process_data.py -max 1 -dp dataset/data2.csv

where:-
     **dataset/data2** should be the path to your dataset csv file
     **max** is a boolean parameter to specify if dataset is maxwell or desharnais

to get more information on how to use the script run
process_data.py -h

#Write on how use train.py script
to run a new training you can use this code

reset && python3 train.py -max 1 -xtdp dataset/maxwell_X_train_sca.csv -ytdp dataset/maxwell_y_train.csv -wkm 1 -sm 0

[for maxwell with kmeans]

or 

reset && python3 train.py -max 0 -xtdp dataset/desh_X_train_sca.csv -ytdp dataset/desh_y_train.csv -wkm 1 -sm 0

[for desharnais with kmeans]

For more information on how to use the script run
reset && python3 train.py -h

*TODO* Write on how to use the test.py script
to run the program on a new testset you can use this code

reset && python3 test.py -max 1 -xvdp dataset/maxwell_X_test_sca.csv -yvdp dataset/maxwell_y_test.csv -vm saved_model/maxwell_leaners.joblib
[for maxwell]

or

reset && python3 test.py -max 0 -xvdp dataset/desh_X_test_sca.csv -yvdp dataset/desh_y_test.csv -vm saved_model/desh_without_kmean_leaners.joblib
[for desharnais]


for more information on the script run 
reset && python3 test.py -h

*TODO* Write on the model.py script
The model.py script, is the script that contains the code implementation of stackensemble.

## Documentation
to see other arguments that can be passed to the train scrip run this command
python3 train.py -h

to see other arguments that can be passed to the test scrip run this command
python3 test.py -h

to see other arguments that can be passed to the process_data script run this command
python3 process_data.py -h


### Results for test datasets
| dataset                                             | accuracy(%) | f1 score(%) | precision(%) |recall(%) |loss           |
|-----------------------------------------------------|------------ |-------------|--------------|----------|---------------|
|hold-out testset(Maxwell -- KMeans -- KNN -- Lasso)  |  1.0        | 1.0         | 1.0          | 1.0      |41683019.4252  |
|hold-out testset(Maxwell -- KNN -- Lasso)            |  0.9231     | 0.9211      | 0.9316       | 0.9231   |123932711.3298 |
|hold-out testset(desh -- KMeans -- KNN -- Lasso)     |  1.0        | 1.0         | 1.0          | 1.0      |4071683.5590   |
|hold-out testset(desh -- KNN -- Lasso)               |  1.0        | 1.0         | 1.0          | 1.0      |4425454.1990   |
||||||


### Sizes of Datasets used
| dataset   |      size     |
|-----------|---------------|
|maxwell    |  63        |
|desharnais |  81         |

### Results on dataset splitting for maxwell
| dataset            |      size     |
|--------------------|---------------|
|train set           |  50        |
|validation set      |  13         |
||||||

### Results on dataset splitting for desharnais
| dataset            |      size     |
|--------------------|---------------|
|train set           |  64        |
|validation set      |  17         |
||||||
