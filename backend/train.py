# from process_data import *
from model import StackEnsemble
from sklearn.svm import SVR,SVC,LinearSVC
from sklearn.linear_model import LinearRegression,Lasso, Ridge, Perceptron, BayesianRidge, LogisticRegression, LassoCV, SGDRegressor
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.ensemble import StackingRegressor, StackingClassifier, RandomForestClassifier
from sklearn.metrics import mean_squared_error
from joblib import dump, load
import  numpy as np
import pickle,argparse,time

#parser
def build_argparser():
    """
    Parse command line arguments.

    :return: command line arguments
    """
    parser = argparse.ArgumentParser("Train a model")

    # -- Add required and optional groups
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')

    required.add_argument('-max', "--maxwel_dset", type=int, help="Specify if dataset to be worked on is maxwell or desharnais.")
    required.add_argument("-xtdp", "--Xtrain_datapath", required=True, type=str, 
                            help="csv file that containing Xtrain on.")

    required.add_argument("-ytdp", "--ytrain_datapath", required=True, type=str, 
                            help="csv file that containing ytrain.")
    
    optional.add_argument("-wkm", "--with_kmeans", type=int, default=0,
                            help="train with kmeans.")

    optional.add_argument("-tm", "--testmodel", type=str, default=None,
                            help="path to .joblib file with a trained model.")
    
    optional.add_argument("-ts", "--traindata_is_scaled", type=int, default=1,
                            help="to load data with scaling or without scaling")


    optional.add_argument('-sp', "--scaler_path", type=str, default=None, 
                            help="path to pretrained scaler, used to scale the train dataset")

    optional.add_argument('-sm', "--save_model", type=int, default=0, help="Save trained model?.")
    optional.add_argument('-mon', "--model_out_name", type=str, default='model', help="name to save the model as.")
    return parser

def main(args):
    dataset_type,range_ =  ('desh', StackEnsemble.create_range([0, 3000])) if not args.maxwel_dset else ('maxwell',StackEnsemble.create_range([0, 5000]))
    print(f'dtype --> {dataset_type}')
    save_learners, model_path = (args.save_model,args.model_out_name)
    traindata_is_scaled = True
    xtrain_path,ytrain_path = args.Xtrain_datapath,args.ytrain_datapath
    with_kmeans, train_levels = args.with_kmeans, 2
    # exit(0)
    scaler_path = args.scaler_path

    level_model = [
        
    			[KNeighborsRegressor(n_neighbors=2, leaf_size=2), Lasso(max_iter=3000, tol=1e-2)],
    			[Lasso(max_iter=3000, tol=1e-2)]
    			
    		  ]


    #Initialize Class That will be Used to Scale the Input Using Formular (z=(x-mean)/std)
    #mean is the mean of the train data, std is the standard diviation from the train data
    #TODO (load previously saved checkpoints)

    #load data
    #load dataset
    if traindata_is_scaled:
        X_train_sca, y_train = np.loadtxt(xtrain_path, delimiter=','), np.loadtxt(ytrain_path, delimiter=',')
    else:
        #TODO (write scripts to use saved scalers)
        scaler_X = load(scaler_path)
        X_train, y_train = np.loadtxt(xtrain_path, delimiter=','), np.loadtxt(ytrain_path, delimiter=',')
        X_train_sca = scaler_X.transform(X_train)

    #load model
    learners = StackEnsemble(levels=train_levels, level_model=level_model, dataset_name=dataset_type)
    learners.fit(X=X_train_sca, y=y_train, with_kmeans=with_kmeans,classification=False)

    print(f'shape shape  --> {X_train_sca.shape}')

    #load model
    preds = learners.predict(X_train_sca,prob_score=False)[0][0].reshape(-1)
    print(f'preds --> {preds} target --> {y_train} rang3 --> {range_}')
    rmse = mean_squared_error(y_train, preds)
    preds = np.array(learners.label_target(preds, range_))
    y_train = np.array(learners.label_target(y_train, range_))
    print(f'preds11 --> {preds}  true --> {y_train}')

    #check if for max of not
    max_flag = False if not args.maxwel_dset else True
    acc, f1_score, rec, pre = learners.check_result(target = y_train, preds = preds, to_cat=False, range_=None,maxwell=max_flag)
    print(f'acc --> {acc}, \nf1_score --> {f1_score} \nprecision --> {pre} \nrecall --> {rec} rmse --> {rmse}')

    #save model
    if save_learners:
        print('Saving Model')
        dump(learners, model_path)
    return

# print(learners.check_result(np.array([[3],[2],[4],[3],[5600],[77]]),np.array([[3],[2],[4],[3],[5],[6]])))

if __name__ == "__main__":
# reset && python3 train.py -tdp dataset/labels/test_new1.csv -tdr dataset/Images/test1/ -vdr dataset/Images/test2/ -vdp dataset/labels/test_new2.csv -tm models/other_models/modelsmodel13_train.pt -vm models/other_models/modelsmodel12_val.pt -mon 'modelsmodel14'
    args = build_argparser().parse_args()
    start = time.time()
    main(args)
    print(f'Training completed in {(time.time()-start)/60} mins')
