[Data Processing Step]

In This Project, There are mainly 3 important Files to note, the *process_data.py, model.py and train.py*. 
The first file *process_data.py* is where all the code to process out data will be created, the second *model.py*
is the file where all the code to create our algorithm will be created, lastly the file *train.py* is the file 
where we will call the functions from *process_data.py and model.py* and where the training will occur.

                                        <-- Scraping Data -->
This Data Used For this Project was gotten from http://promise.site.uottawa.ca/SERepository/datasets/desharnais.arff. Because of the way the Data is on the Site, The was copied and it was arranged into a csv file. A Bit Of Preprocessing Went into Getting it into the right format.

                                <-- Filling Missing Values Using MICE -->
After Getting Our Data in the right Format Where we can Work with it, We Needed to EnSure Our Algorithm Can work Efficiently With Sure Data, To Accomplish This, We Had to Take Care of Missing Values. Cases Of Missing Values Occur In a dataset Due to various Reasons, one can be that there was an error when Inputting values for that instance, another can be that Such data was omitted during conversion from one format to another or the data for that instance is not Just Available. Initially an Univariate Approach Of filling Missing Values Such as using Mean, Median etc of a Column was Suggested But Due to the amount Of bias this method can introduce to the dataset a Multivariate  approach was Used instead. The Exact Multivariate Used is the Multivariate imputation by chained equations (MICE) Implemented In Sklearn, a popular Package for Data Wrangling and Machine Learning. Due to The Uncertainty this method tend to take care of (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3074241/#mpr329-bib-0015)
it was the ideal method to use. Since the way the algorithm works is Such that it learns the relationship of all the features in a dataset with each other, We didn't have to worry about if the proposed value for the missing data was off. The Code That is Responsible for this whole process is created in the file *process_data.py(line 78)* and is called in the file *train.py(line 7,8 and 19)* where the Whole Operation Took place.

                                 <-- Spliting Data Using ShuffleSplit -->
Spliting the Data Into Train and Test Was Fairly Easy, 90percent of the data went for train, while the rest of it 10percent went for test. To Get this done We used The Class ShuffleSplit in sklearn package Which helps Shuffle our data Set before splitting. The code to perform this Operation Was created in the file *process_data.py(line 56)* and was called in *train.py(line 22)*

                                 <-- Feature Scaling With StandardScaler-->
According to Research machine learning algorithm have been known to do well when their feature are been scaled, could this be a defect? maybe, maybe not. So Scaling is when the range of value for each feature in the dataset are the same, Various methods are used for this But For this Project We Made Use Of Standardizatoin, Which simply means Subtracting the mean of the feature from each data and dividing by the standard deviation of all the features. This method is said to not be affected by outliers in the 
dataset. So To Scale Our data we made Use of the Sklearn Class StandardScaler. The code to perform this Operation was Created in *train.py (line 13)* and called in *train.py (line 28)*.