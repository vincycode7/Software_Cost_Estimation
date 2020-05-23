import pandas as pd
import numpy as np
import pandas,numpy

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedShuffleSplit,ShuffleSplit

# def txt_to_excel(file='fromweb.txt',save_to="software_ce_data.xlsx"):
#     lst = []
#     box = []
#     with open(file) as f:
#         for each in f.readlines():
#             for each_one in each[:-1].split(','):
#                 if each_one == '?':
#                     lst.append('NaN')
#                 elif each_one == '':
#                     pass
#                 else:
#                     lst.append(int(each_one))
#             box.append(lst)
#             lst = []

#     data = pd.DataFrame(box,columns=['Project','TeamExp','ManagerExp','YearEnd','Length','Effort','Transactions','Entities','PointsAdjust','Envergure','PointsNonAjust','Langage'])
#     data.to_excel(save_to,index=False,sheet_name='Sheet_name_1')


# def csv_to_ext(file_name='fromweb.csv',ext='cs'):
#     """
#         This is a function Used to Preprocess the data
#     """
    
#     #Read in data
#     data = pd.read_csv(file_name)
    
#     #Replace Missing Value With Recognized Missing Value
#     data.replace(['?','? ',' ?',' ? ','',' '],np.nan,inplace=True)
    
#     #Drop Some Columns
#     data.drop(axis=1, columns=['Project'], inplace=True)
    
#     #ReIndex
#     col = list(data.columns)
#     col.remove('Effort')
#     col.append('Effort')
#     data = data.reindex(columns=col,)
    
#     #save new data
#     out_filename = file_name.split('.')[0]+'1.csv'
#     data.to_csv(out_filename)
def Split_Datato_Half(X,y,train_ratio=0.8,Stratified=False):
    supported = [numpy.ndarray, pandas.core.frame.DataFrame]
    if type(X) not in supported or type(y) not in supported: 
        raise ValueError(f'X is {type(X)} and y is {type(y)}, both values are expected to be either numpy array or a pandas dataframe')

    split_data = StratifiedShuffleSplit(n_splits=1, train_size=train_ratio) if Stratified else ShuffleSplit(n_splits=1, train_size=train_ratio)
    
    #split the data into two halves
    try:
        X,y = X.values, y.values
    except:
        X,y = X,y

    for train_index, test_index in split_data.split(X, y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
    return (X_train,y_train), (X_test, y_test)

class Fill_Empty_Spaces(BaseEstimator, TransformerMixin):
    """
        This is a Class Used to Preprocess the data
    """
    
    def __init__(self, features=['TeamExp', 'ManagerExp', 'YearEnd','Length', 
                                                             'Transactions','Entities','PointsAdjust', 
                                                             'Envergure','PointsNonAjust', 'Langage','Effort']):
    
        #Read in data
        self.features = features

    def fit(self,X):
        return self #do nothing
    def transform(self,X):
        """
            Work on the dataset
        """
        
        try:
            X = X[self.features]
        except Exceptions as exp:
            raise exp
            
        #Replace Missing Value With Recognized Missing Value
        X.replace(['?','? ',' ?',' ? ','',' ','-'],np.nan,inplace=True)
        
        return X
    
    
class Round_Of_Values(BaseEstimator, TransformerMixin):
    """
        This is a Class Used to Preprocess the data
    """
    
    def __init__(self, all_feat=['TeamExp', 'ManagerExp', 'YearEnd','Length', 
                                                             'Transactions','Entities','PointsAdjust', 
                                                             'Envergure','PointsNonAjust', 'Langage','Effort'],feat_to_round=['TeamExp', 'ManagerExp','YearEnd','Length','Langage']):
    
        #Read in data
        self.feat_to_round = feat_to_round
        self.all_feat = all_feat

    def fit(self,X):
        return self #do nothing
    
    def transform(self,X):
        """
            Round Of Values In Features
        """
        
        try:
            X = pandas.DataFrame(X,columns=self.all_feat)
        except Exceptions as exp:
            raise exp
            
        X[self.feat_to_round] = X[self.feat_to_round].apply(lambda x: round(x,0)).copy()
        
        #SPlit into feature and y
        X,y = X[X.columns[:-1]].copy(), X[[X.columns[-1]]].copy()
        
        return X,y