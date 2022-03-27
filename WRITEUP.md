[Data Processing Step](Step 1)

In This Project, There are mainly 3 important Files to note, the *process_data.py, model.py and train.py*. 
The first file, *process_data.py* is where all the code to process data will be created, the second file, *model.py*
is the file where all the code to create our algorithm will be created, lastly the file, *train.py* is the file 
where we will call the functions in *process_data.py and model.py* and it is where the training will occur.

                                        <-- Scraping Data -->
The Data Used For this Project can be gotten from http://promise.site.uottawa.ca/SERepository/datasets/desharnais.arff and https://github.com/vincycode7/MIERatio/tree/master/datasets. Because of the way the Data is on the Site, The data was copied and it was arranged into a csv file. A Bit Of Preprocessing Went into Getting it into the right format.

                                <-- Encode Feature Label (SPECIFIC TO MAXWELL DATASET)-->
Since the maxwell dataset contained some features that are categorical in nature e.g (good, bad, fair) this features needed to be converted into numerical labels first before Missing values are filled this is as a result of the technique we are using to fill in missing values, After the numerical labeling is done good for install becomes 1, bad becomes 2 fair becomes 3 and missing values are set to NaN, this was we can easily fill in missing values using *Multivariate imputation by chained equations (MICE)*.


                                <-- Filling Missing Values Using MICE -->
After Getting Our Data in the right Format Where we can Work with it, We Needed to EnSure Our Algorithm Can work Correctly With Such Data, To Accomplish This, We Had to First Take Care of Missing Values. Cases Of Missing Values Occur In a dataset Due to various Reasons, one can be that there was an error when Storing values for that instance, another can be that Such data was omitted during conversion from one format to another or maybe the data for that instance is not Just Available. Initially a Univariate Approach Of filling Missing Values Such as Filling Missing Values with the Computed Mean or Median of a Column, But Due to the amount Of bias this method can introduce to the dataset a Multivariate  approach was Used instead. The Exact Implementation of Multivariate Used is the *Multivariate imputation by chained equations (MICE)* Which is Implemented In Sklearn, a popular Package for Data Wrangling and Machine Learning. Due to The Uncertainty this method tend to take care of (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3074241/#mpr329-bib-0015)
it was the ideal method to use. Since the way the algorithm works is Such that it learns the relationship of all the features in a dataset with each other to determine what the misisng value could be, We didn't have to worry much about if the proposed value for the missing data was bias. The Code That is Responsible for this whole process is created in the file *process_data.py(line 78)* and is called in the file *train.py(line 7,8 and 19)* where the Whole Operation Took place.

                                 <-- Spliting Data Using ShuffleSplit -->
Spliting the Data Into Train and Test Was Fairly Easy, 80percent of the data went for training, while the rest of it 20percent went for testing. To Get this done We used The *Class ShuffleSplit* in sklearn package Which helps Shuffle a data Set before splitting. The code to perform this Operation Was created in the file *process_data.py(line 56)* and was called in *train.py(line 22)*

                                        <-- OneHotEncode_Columns (SPECIFIC TO MAXWELL DATASET)-->
To avoid misintepretation from the network some features had to be One Hot Encoded. For instance in this sample (good--1, bad--2 and fair--3) Misinterpretation can occur if a network learns to reward fair and bad for their high label values instead of treatnig them equally and learns to punish good for it's low label, so to avoid this kind of misinterpretation from the data  we decided to One-Hot Encode such features.

                                 <-- Feature Scaling With StandardScaler-->
According to Research machine learning algorithms tend to do converge faster when their feature are been scaled, could this be a defect? maybe, maybe not. Scaling is when the range of value for each feature in the dataset are recalculated such that the the range is the same across features, Various methods can be used for this But For this Project We Made Use Of Standardization, Which simply means Subtracting the mean of the features from each value and dividing by the standard deviation of all the features. This method is said to not be affected by outliers in the dataset. So To Scale Our data we made Use of the *Sklearn Class StandardScaler*. The code to perform this Operation was Created in *train.py (line 13)* and called in *train.py (line 28)*. *(range to convert), *(standardization formular), 

                                            <-- Output Range -->
Once processing was done, there was a need to convert the target to catigorical targets for evaluations purpose only, this the problem maintained it's nature as a regression problem for training but was converted to a categorical problem when it came to evaluation. This was done due to the limited samples of dataset, So to better estimate the outputs of the model, there were converted to range of values. For maxwell dataset, the range of values are, [0-5000] and [>5000]. For desharnais the range of values are [0-3000] and [>3000].

[Creating Model Architecture](Step 2)
The model used in this project is a stacked ensemble model and in three layers, for the first layer a cluster algorithm is used this algorithm is the kmeans algorithm. for the second layer the base-learners two algorithms are used first is the lasso regression algorithm and the second is the KNN algorithm. for the third layer(meta-learner) which is the last layer lasso regression was used.

[Training Model](Step 3)
The whole training process begins by passing the processed data through the first layer(cluster algorithm). The cluster algorithm splits the dataset into n clusters, where n is the number of base learners in the stacked model. the second layer of the model involves the n base learners to take in their respective dataset in the order in which they came out of the cluster algorithm. Each base learners trains on their dataset and after training is done, they all make predictions on all the dataset combine, the output of this predictions is combined and feed into the last layer which is the meta learner(s). this meta-learner(s) then trains on the outputs of the base-learner.


[Testing Model](Step 4)
Once Training was done, the performance of the model was tested using a hold-out dataset(20percent of the original dataset). 


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

[Summary](Step 5)
##Additional Explanations
From the result of the research, even though there was little of no change in the accuracy, f1_score, recall, precision of the models with application of kmeans, we observe that there was significant drop in the loss with means the application of kmeans improved the predicting power of each model.