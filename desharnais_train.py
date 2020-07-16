from process_data import *

if __name__ == "__main__":

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

    #Initialize Class That will be Used to Scale the Input Using Formular (z=(x-mean)/std)
    #mean is the mean of the train data, std is the standard diviation from the train data
    scaler = StandardScaler()

    #Read In Data
    data = pd.read_csv('dataset/fromweb.csv',)

    #Process Data
    data = process_pipeline.fit_transform(data)

    #SPlit into feature and y
    y = data[['Effort']]
    X = data.drop(columns='Effort').copy()
    del data
    
    #Split Data to Train and Test
    (X_train, y_train), (X_test, y_test) = Split_Datato_Half(X,y,train_ratio=0.9,Stratified=False)
    
    #Fit scaler to train set
    X_train = scaler.fit_transform(X=X_train)

    #transform test set
    X_test = scaler.transform(X=X_test)

    
    