from process_data import *

if __name__ == "__main__":

  #Initialize Pipeline
  process_pipeline = Pipeline([
                    ('Process_Data', Fill_Empty_Spaces()),
                    ('Mice_Imputer', IterativeImputer(max_iter=10, random_state=0)),
                    ('Round_of_Values', Round_Of_Values())])
  
  #Initialize Class That will be Used to Scale the Input Using Formular (z=(x-mean)/std)
  #mean is the mean of the train data, std is the standard diviation from the train data
  scaler = StandardScaler()

  #Read In Data
  data = pd.read_csv('fromweb.csv',)

  #Process Data
  X,y = process_pipeline.fit_transform(data)

  #Split Data to Train and Test
  (X_train, y_train), (X_test, y_test) = Split_Datato_Half(X,y,train_ratio=0.9,Stratified=False)

  #Fit scaler to train set
  X_train = scaler.fit_transform(X=X_train)

  #transform test set
  X_test = scaler.transform(X=X_test)