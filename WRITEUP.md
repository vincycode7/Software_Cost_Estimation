[Data Processing Step]


                                        <-- Scraping Data -->
This Data Used For this Project was gotten from http://promise.site.uottawa.ca/SERepository/datasets/desharnais.arff. Because of the way the Data is on the Site, The was copied and it was arranged into a csv file. A Bit Of Preprocessing Went into Getting it into the right format.

                                <-- Filling Missing Values Using MICE -->
After Getting Our Data in the right Format Where we can Work with it, We Needed to EnSure Our Algorithm Can work Efficiently With Sure Data, To Accomplish This, We Had to Take Care of Missing Values. Cases Of Missing Values Occur In a dataset Due to various Reasons, one can be that there was an error when Inputting values for that instance, another can be that Such data was omitted during conversion from one format to another or the data for that instance is not Just Available. Initially an Univariate Approach Of filling Missing Values Such as using Mean, Median etc of a Column was Suggested But Due to the amount Of bias this method can introduce to the dataset a Multivariate  approach was Used instead. The Exact Multivariate Used is the Multivariate imputation by chained equations (MICE) Implemented In Sklearn, a popular Package for Data Wrangling and Machine Learning. Due to The Uncertainty this method tend to take care of (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3074241/#mpr329-bib-0015)
it was the ideal method to use. Since the way the algorithm works is Such that it learns the relationship of all the features in a dataset with each other, We didn't have to worry about if the proposed value for the missing data was off.

                                 <-- Spliting Data Using ShuffleSplit -->


                                 <-- Feature Scaling With StandardScaler-->