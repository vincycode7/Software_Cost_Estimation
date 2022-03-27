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
    required.add_argument("-xvdp", "--Xval_datapath", required=True, type=str,
                            help="folder path that containing Xval.")
    required.add_argument("-yvdp", "--yval_datapath", required=True, type=str, 
                            help="csv file that containing yval.")

    required.add_argument("-vm", "--valmodel", type=str, required=True, help="path to .pt or pth file with a trained model.")
    optional.add_argument('-sp', "--scaler_path", type=str, default=None, help="path to pretrained scaler, used to scale the train dataset")
    return parser

def main(args):
    # 3000 for `desh` and 5000 for `maxwell` we would get a 100% accuracy
    dataset_type,range_ =  ('desh', StackEnsemble.create_range([0, 3000])) if not args.maxwel_dset else ('maxwell',StackEnsemble.create_range([0, 5000]))
    print(f'dtype --> {dataset_type}')
    model_path = args.valmodel
    testdata_is_scaled = True
    xtest_path, ytest_path = args.Xval_datapath, args.yval_datapath
    scaler_path = args.scaler_path

    #Initialize Class That will be Used to Scale the Input Using Formular (z=(x-mean)/std)
    #mean is the mean of the train data, std is the standard diviation from the train data
    #TODO (load previously saved checkpoints)
        
    if testdata_is_scaled:
        X_test_sca, y_test = np.loadtxt(xtest_path, delimiter=','), np.loadtxt(ytest_path, delimiter=',')
    else:
        #TODO (write scripts to use saved scalers)
        scaler_X = load(scaler_path)
        X_test, y_test = np.loadtxt(xtest_path, delimiter=','), np.loadtxt(ytest_path, delimiter=',')
        X_test_sca = scaler_X.transform(X_test)   

    print(f'range --> {range_}  {model_path}')
    learners = load(model_path)
    preds = learners.predict(X_test_sca,prob_score=False)[0][0].reshape(-1)
    print(f'preds --> {preds} target --> {y_test} rang3 --> {range_}')
    rmse = mean_squared_error(y_test, preds)
    preds = np.array(learners.label_target(preds, range_))
    y_test = np.array(learners.label_target(y_test, range_))
    print(f'preds11 --> {preds}  true --> {y_test}')
    max_flag = False if not args.maxwel_dset else True
    acc, f1_score, rec, pre = learners.check_result(target = y_test, preds = preds, to_cat=False, range_=None,maxwell=max_flag)
    print(f'acc --> {acc}, \nf1_score --> {f1_score} \nprecision --> {pre} \nrecall --> {rec} rmse --> {rmse}')

# print(learners.check_result(np.array([[3],[2],[4],[3],[5600],[77]]),np.array([[3],[2],[4],[3],[5],[6]])))

if __name__ == "__main__":
# reset && python3 train.py -tdp dataset/labels/test_new1.csv -tdr dataset/Images/test1/ -vdr dataset/Images/test2/ -vdp dataset/labels/test_new2.csv -tm models/other_models/modelsmodel13_train.pt -vm models/other_models/modelsmodel12_val.pt -mon 'modelsmodel14'
    args = build_argparser().parse_args()
    main(args)