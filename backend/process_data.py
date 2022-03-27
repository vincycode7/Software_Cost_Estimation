import pandas as pd
import numpy as np
import argparse,time, pandas,numpy

from joblib import dump, load
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

    split_data = StratifiedShuffleSplit(n_splits=1, train_size=train_ratio,) if Stratified else ShuffleSplit(n_splits=1, train_size=train_ratio)
    
    #split the data into two halves
    try:
        X,y = X.values, y.values
    except:
        X,y = X,y

    for train_index, test_index in split_data.split(X, y):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
    return (X_train,y_train), (X_test, y_test)

#parser
def build_argparser():
    """
    Parse command line arguments.

    :return: command line arguments
    """
    parser = argparse.ArgumentParser("Process dataset")

    # -- Add required and optional groups
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')

    required.add_argument('-max', "--maxwel_dset", type=int, help="Specify if dataset to be worked on is maxwell or desharnais.")
    required.add_argument("-dp", "--datapath", required=True, type=str,
                            help="folder path that containing data to be processed.")

    optional.add_argument('-sd', "--split_data", type=int, default=0, required=False, help="if True dataset will be splited")
    optional.add_argument('-sds', "--save_dataset", type=int, default=0, required=False, help="if True process dataset will be saved")
    optional.add_argument('-sp', "--scalar_split", type=int, default=0, required=False, help="if True data will be scaled")
    optional.add_argument('-ss', "--save_scalar", type=int, default=0, required=False, help="if True model used to scale data will be saved will be saved")
    return parser

def main(args):
    dataset_type, rawdata_name =  ('desh',args.datapath) if not args.maxwel_dset else ('maxwell',args.datapath)
    split_data, scaler_split, save_dset, save_scaler = args.split_data, args.scalar_split, args.save_dataset, args.save_scalar
    xtrain_path,ytrain_path = 'dataset/'+ dataset_type+'_X_train_sca.csv','dataset/'+ dataset_type+'_y_train.csv'
    xtest_path, ytest_path = 'dataset/'+ dataset_type+'_X_test_sca.csv', 'dataset/'+ dataset_type+'_y_test.csv'
    # dataset_type, rawdata_name =  ('desh','dataset/fromweb.csv') if not args.maxwel_dset else ('maxwell','dataset/data2.csv')
    # data_pipline_path = 'saved_model/'+ dataset_type+'_data_pipeline.joblib'
    # load_data_pipline, load_scaler, scaler_split = False, False, True
    # save_data_pipline = not True, 

    scaler_path = 'saved_model/'+ dataset_type+'_scaler.joblib'

    #seed
    if 'max' in dataset_type:
        print('maxwell')
        model_name = 'saved_model/maxwell.joblib'
        all_features = ['size_D', 'duration_D', 'app', 'har', 'dba', 'ifc', 'source', 'nlan',
                'telonuse', 't01', 't02', 't03', 't04', 't05', 't06', 't07', 't08',
                't09', 't10', 't11', 't12', 't13', 't14', 't15','effort_D']
        find_in = [ 'app', 'har', 'dba', 'ifc', 'source','telonuse']

        #Initialize Pipeline
        process_pipeline = Pipeline([
                        ('fill_missing_for_cat1', Fill_Empty_Spaces(all_features=all_features,find_in=find_in,with_='NaN')),
                        ('encode_cat_fea', Encode_Feature_Label(all_features=all_features, to_encode=find_in)),
                        ('fill_missing_for_cat2', Fill_Empty_Spaces(all_features=all_features,find_in=find_in,with_=np.nan)),
                        ('Mice_Imputer', IterativeImputer(max_iter=20, random_state=0)),
                        ('Round_of_Values', Round_Of_Values(all_feat=all_features,feat_to_round=all_features)),
                        ('one_hot_encode', OneHotEncode_Columns(all_feat=all_features, feat_to_dummy=find_in+['nlan']))
                        ]) 
                    # if not load_data_pipline else load(data_pipline_path)

        #save data at each preprocessing level
        #Read In Data(1)
        print(rawdata_name)
        data = pd.read_csv(rawdata_name)

        #Process Data
        data = process_pipeline.fit_transform(data)
        print(data)
        data.to_csv("./precrossing_data_ouput/maxwell/after_one_hot_encoding.csv", index=False)
        # np.savetxt("./precrossing_data_ouput/maxwell/after_mice_imputer.csv", data, delimiter=',')
    elif 'desh' in dataset_type:
        model_name = 'saved_model/desh.joblib'
        print('desh')
        all_features = ['TeamExp', 'ManagerExp', 'YearEnd','Length', 
                        'Transactions','Entities','PointsAdjust', 
                        'Envergure','PointsNonAjust', 'Langage','Effort']

        find_in = [ 'TeamExp', 'ManagerExp','YearEnd','Length',
                    'Langage']

        #Initialize Pipeline
        process_pipeline = Pipeline([
                        ('fill_missing_for_cat', Fill_Empty_Spaces(all_features=all_features,find_in=find_in,with_='NaN')),
                        ('Mice_Imputer', IterativeImputer(max_iter=10, random_state=0)),
                        ('Round_of_Values', Round_Of_Values(all_feat=all_features,feat_to_round=all_features))
                        ]) 
                    # if not load_data_pipline else load(data_pipline_path)

        #save data at each preprocessing level
        #Read In Data(1)
        print(rawdata_name)
        data = pd.read_csv(rawdata_name)

        #Process Data
        data = process_pipeline.fit_transform(data)
        print(data)
        data.to_csv("./precrossing_data_ouput/desh/after_round_off_value.csv", index=False)
        # np.savetxt("./precrossing_data_ouput/desh/fill_nan_with_mice_imputer.csv", data, delimiter=',')

    else:
        #TODO fix this place
        raise ValueError('provide dataset processing pipline')

    
    #Initialize Class That will be Used to Scale the Input Using Formular (z=(x-mean)/std)
    #mean is the mean of the train data, std is the standard diviation from the train data
    #TODO (load previously saved checkpoints)

    # if split_data:
    #     scaler_X = StandardScaler()
    #     #Read In Data(1)
    #     data = pd.read_csv(rawdata_name)

    #     #Process Data
    #     data = process_pipeline.fit_transform(data)

    #     # if save_data_pipline:
    #     #     dump(process_pipeline, data_pipline_path) 
            
    #     #SPlit into feature and y
    #     y_fea_name = 'effort_D' if 'max' in dataset_type else 'Effort'
    #     y = data[[y_fea_name]]
    #     X = data.drop(columns=y_fea_name).copy()
    #     del data
        
    #     #Split Data to Train and Test
    #     (X_train, y_train), (X_test, y_test) = Split_Datato_Half(X,y,train_ratio=0.8,Stratified=False)
    #     # print('make it?')
        
    #     if scaler_split:
    #         #Fit scaler to train set and test set
    #         X_train_sca, X_test_sca = scaler_X.fit_transform(X=X_train), scaler_X.transform(X=X_test)
            
    #         if save_dset:
    #             np.savetxt(xtrain_path, X_train_sca, delimiter=','), np.savetxt(ytrain_path, y_train, delimiter=',')
    #             np.savetxt(xtest_path, X_test_sca, delimiter=','), np.savetxt(ytest_path, y_test, delimiter=',') 

    #         if save_scaler:
    #             dump(scaler_X, scaler_path)    

    #     else:
    #         if save_dset:
    #             # print(2235)
    #             np.savetxt(xtrain_path, X_train, delimiter=','), np.savetxt(ytrain_path, y_train, delimiter=',')
    #             np.savetxt(xtest_path, X_test, delimiter=','), np.savetxt(ytest_path, y_test, delimiter=',')     

# print(learners.check_result(np.array([[3],[2],[4],[3],[5600],[77]]),np.array([[3],[2],[4],[3],[5],[6]])))

if __name__ == "__main__":
    args = build_argparser().parse_args()
    main(args)
    pass