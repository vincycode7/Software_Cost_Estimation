from process_data import *

if __name__ == "__main__":

  #Initialize Pipeline
  process_pipeline = Pipeline([
                    ('Process_Data', Fill_Empty_Spaces()),
                    ('Mice_Imputer', IterativeImputer(max_iter=10, random_state=0)),
                    ('Round_of_Values', Round_Of_Values())])

  #Read In Data
  data = pd.read_csv('fromweb.csv',)

  #Process Data
  X,y = process_pipeline.fit_transform(data)

  
  print(X.head())