import pandas as pd
import numpy as np
import pandas,numpy

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.model_selection import train_test_split
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,LabelEncoder
from sklearn.model_selection import StratifiedShuffleSplit,ShuffleSplit


class Encode_Feature_Label(BaseEstimator, TransformerMixin):
    """
        This is a Class Used to Preprocess the data, By
        encoding N features and filling missing values
        too
    """
    
    def __init__(self, all_features=['size_D', 'duration_D', 'app', 'har', 
                                    'dba', 'ifc', 'source', 'nlan',
                                    'telonuse', 't01', 't02', 't03', 
                                    't04', 't05', 't06', 't07', 't08',
                                    't09', 't10', 't11', 't12', 't13', 
                                    't14', 't15'],  
                        
                        to_encode=['app','har', 'dba', 'ifc', 'source', 
                                    'nlan','telonuse']):
    
        #Read in data
        self.features = all_features
        self.to_encode = to_encode

    def fit(self,X):
        #check if features are present
        try:
            X = X[self.features]
        except Exception as exp:
            raise exp

        self.all_encode = {each_feature : LabelEncoder().fit(X[each_feature]) for each_feature in self.to_encode}
        return self #do nothing

    def transform(self,X):
        """
            Work on the dataset
        """
        #check if features are present
        try:
            X = X[self.features]
        except Exception as exp:
            raise exp
            
        #Replace Labels with numerical values
        for each_feature in self.to_encode:
            X[each_feature] = self.all_encode[each_feature].transform(X[each_feature])
            classes_ = self.all_encode[each_feature].classes_
            none_index = np.where(classes_ == 'NaN')[0]
            if none_index.shape[0] >= 1:
                none_index = int(none_index)
                X[each_feature].replace(none_index,np.nan,inplace=True)
        return X


class Fill_Empty_Spaces(BaseEstimator, TransformerMixin):
    """
        This is a Class Used to Preprocess the data, By
        Filling Missing Values with Standard Values That
        Represents Missing Values, e.g numpy.nan.
    """
    
    def __init__(self, all_features=[   'TeamExp', 'ManagerExp', 'YearEnd','Length', 
                                        'Transactions','Entities','PointsAdjust', 
                                        'Envergure','PointsNonAjust', 'Langage','Effort'],

                        find_in=[   'TeamExp', 'ManagerExp', 'YearEnd','Length', 
                                    'Transactions','Entities','PointsAdjust', 
                                    'Envergure','PointsNonAjust', 'Langage','Effort'],
                                        
                        find=None,
                        with_=None
                        ):
    
        #Read in data
        self.features = all_features
        self.find_in = find_in
        self.find = ['?','? ',' ?',' ? ','',' ','-',None,'None','none','Null','null',np.nan] if not find else find
        self.with_ = np.nan if not with_ else with_

    def fit(self,X):
        return self #do nothing
    def transform(self,X):
        """
            Work on the dataset
        """
        
        try:
            X = X[self.features]
        except Exception as exp:
            raise exp
            
        #Replace Missing Value With Recognized Missing Value
        X[self.find_in] = X[self.find_in].replace(self.find,self.with_)
        return X
    
    
class Round_Of_Values(BaseEstimator, TransformerMixin):
    """
        This is a Class Used to Preprocess the data 
        by rounding off value to nearest integer.
    """
    
    def __init__(self, all_feat=['TeamExp', 'ManagerExp', 'YearEnd','Length', 
                                'Transactions','Entities','PointsAdjust', 
                                'Envergure','PointsNonAjust', 'Langage','Effort'],
                                
                        feat_to_round=['TeamExp', 'ManagerExp','YearEnd','Length',
                                'Langage']):
    
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
        except Exception as exp:
            raise exp
            
        X[self.feat_to_round] = X[self.feat_to_round].apply(lambda x: round(x)).astype('int')
        
        return X

class OneHotEncode_Columns(BaseEstimator, TransformerMixin):
    """
        This is a Class Used to Preprocess the data by
        one hot encoding of specified features.
    """
    
    def __init__(self, all_feat=['TeamExp', 'ManagerExp','YearEnd','Length',
                                'Langage'],feat_to_dummy=['TeamExp', 'ManagerExp','YearEnd','Length',
                                'Langage']):
    
        #Read in data
        self.feat_to_dummy = feat_to_dummy
        self.all_feat = all_feat
    def fit(self,X):
        return self #do nothing
    
    def transform(self,X):
        """
            One Hot Encode Some Features 
        """
        
        try:
            X = X[self.all_feat]
        except Exception as exp:
            raise exp
            
        X = pd.get_dummies(X,columns=self.feat_to_dummy)
        return X

def Split_Datato_Half(X,y,train_ratio=0.8,Stratified=False):
    """
        This Function Utilizes the Split Functions in Sklearn 
        to Split that into Two halves.
    """
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