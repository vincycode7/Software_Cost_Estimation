from process_data import *
from model import StackEnsemble
from sklearn.svm import SVR
if __name__ == "__main__":
    all_features = ['size_D', 'duration_D', 'app', 'har', 'dba', 'ifc', 'source', 'nlan',
            'telonuse', 't01', 't02', 't03', 't04', 't05', 't06', 't07', 't08',
            't09', 't10', 't11', 't12', 't13', 't14', 't15','effort_D']
    find_in = [ 'app', 'har', 'dba', 'ifc', 'source','telonuse']

    #Initialize Pipeline
    process_pipeline = Pipeline([
                    ('fill_missing_for_cat1', Fill_Empty_Spaces(all_features=all_features,find_in=find_in,with_='NaN')),
                    ('encode_cat_fea', Encode_Feature_Label(all_features=all_features, to_encode=find_in)),
                    ('fill_missing_for_cat2', Fill_Empty_Spaces(all_features=all_features,find_in=find_in,with_=np.nan)),
                    ('Mice_Imputer', IterativeImputer(max_iter=10, random_state=0)),
                    ('Round_of_Values', Round_Of_Values(all_feat=all_features,feat_to_round=all_features)),
                    ('one_hot_encode', OneHotEncode_Columns(all_feat=all_features, feat_to_dummy=find_in+['nlan']))])

    #Initialize Class That will be Used to Scale the Input Using Formular (z=(x-mean)/std)
    #mean is the mean of the train data, std is the standard diviation from the train data
    scaler = StandardScaler()

    #Read In Data
    data = pd.read_csv('dataset/data2.csv')

    #Process Data
    data = process_pipeline.fit_transform(data)

    #SPlit into feature and y
    y = data[['effort_D']]
    X = data.drop(columns='effort_D').copy()
    del data
    
    #Split Data to Train and Test
    (X_train, y_train), (X_test, y_test) = Split_Datato_Half(X,y,train_ratio=0.9,Stratified=False)
    
    #Fit scaler to train set
    X_train_sca = scaler.fit_transform(X=X_train)

    #transform test set
    X_test_sca = scaler.transform(X=X_test)

# from sklearn.cluster import KMeans
# kmeans_instance = KMeans(n_clusters=2,n_init=1000)
# predictions = kmeans_instance.fit_predict(X=X_train_sca, y=y_train)
# print(f'predictons == {predictions}')
# print(f'cluster 1 = {X_train[predictions==0]}, \ncluster 2 {X_train[predictions==1]}')

learners = StackEnsemble(levels=3, level_model=[[SVR,SVR,SVR],[SVR,SVR],[SVR,SVR,SVR]])