from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, f1_score, recall_score, precision_score
import numpy as np

class StackEnsemble:
    def __init__(self,levels=2, level_model=None, with_kmeans=True,dataset_name="default_name"):
        """ 
            This is the stack ensemble trainer that trains on different 
            base learners.

            levels :- Specifies how many levels there are in the training 
            process, where the first level is for base learner and other
            levels is for meta learner.
            
            Example1 levels = 2 : this means level 1 for base learners to learn and level 2
            for meta learners.

            Example2 levels = 7 : this means level 1 for base learners to learn and level 2-6
            for meta learners.


            level_model :- This is where every model(in a list or tuple) is specified for each 
            level and each model-list is stored in an outer list.

            Example 1 level = 2, level_model = [[knn, svm, dt], [svm]]
            Example 2 level = 3, level_model = [[knn, svm, dt], [svm,knn],[svm]]

            note :- the model in the last level should be one else the first model in the last level will be picked.

            Example 3 level = 3, level_model = [[knn, svm, dt], [svm,knn],[svm, knn]] will become [[knn, svm, dt], [svm,knn],[svm]]

            with_kmeans :- this argument will join all dataset into one and try to split them 
            into n base learners.
        """
        assert type(level_model) is list, "the level_model variable should be a list of list(s)" #check if the value of level_model is a list that contains more lists
        for each in level_model: assert type(each) is list, "levels should all be in list"  #check if all levels are in lists
        for each in level_model: assert not len(each)==0,f"size of list should be >=1 {len(each)}"
        self.levels = levels

        assert self.levels == len(level_model), "model levels size should be the same as num of levels levels" #check if model_level size is the same as levels

        #check if model provided, if model evels is greater than 1 and if the last level has two models
        if level_model:
            if len(level_model) > 1:
                if len(level_model[-1]) == 1:
                    pass
                elif len(level_model[-1]) > 1:
                    level_model.append([level_model[-1][0]]) #append a last level model
                    self.levels += 1
                    print(f"warning, added a new level {level_model[-1]} because previous last level is greater than 1")
                else:
                    level_model[-1] = [level_model[-2][0]] #pick the first model in the second to the last level(this might not really be needed though)
            elif len(level_model) == 1:
                if len(level_model[0]) > 1:
                    level_model.append([level_model[0][0]]) #append a last level model
                    self.levels += 1
                    print(f"warning, added a new level {level_model[-1]} because previous last level is greater than 1")
        else: #no model provided
            raise ValueError('No model passed')

        self.models = level_model
        self.registed_level_size = {level_index:len(self.models[level_index]) for level_index in range(len(self.models))}
        self._dataset = None
        self.with_kmeans = None
        self.dataset_name = dataset_name

    def fit(self, X, y, with_kmeans=True, classification=False):
        #check X
        try:
            assert not X, "X is None"
            raise ValueError('1 X is not numpy')

        except:
            try:
                assert (X).any(),"2 X is not numpy"
            except:
                raise ValueError('3 X is not numpy')

        #check X
        try:
            assert not y, "y is None"
            raise ValueError('1 y is not numpy')

        except:
            try:
                assert (y).any(),"2 y is not numpy"
            except:
                raise ValueError('3 y is not numpy')

        self.with_kmeans = with_kmeans

        dset_name_x = 'dataset/'+'with_kmeans_'+ str(self.with_kmeans) +  self.dataset_name+'_x_before_split.csv'
        dset_name_y = 'dataset/'+'with_kmeans_'+ str(self.with_kmeans) +  self.dataset_name+'_y_before_split.csv'
        
        # print(f"Dataset before the split: X: {X} \n")
        np.savetxt(dset_name_y, y, delimiter=',') 

        # print(f"y: {y} \n")
        np.savetxt(dset_name_x, X, delimiter=',') 
        # print(f"together is: {np.concatenate((X,y.reshape(-1,1)),axis=1)}")
        #split with kmeans or not
        self.dataset = self.split_with_kmeans(X,y,n_clusters=len(self.models[0])) if self.with_kmeans else [[X,y]] #returns list of n dataset

        counter=1
        for each_split_dset in self.dataset:
            dset_name_x = 'dataset/'+'with_kmeans_'+ str(self.with_kmeans) + self.dataset_name +'_x'+str(counter)+'_after_split.csv'
            dset_name_y = 'dataset/'+'with_kmeans_'+ str(self.with_kmeans) +  self.dataset_name+'_y'+str(counter)+'_after_split.csv'
            # print(f"counter: {counter}")
            # print(f"Dataset after the split: X: {each_split_dset[0]} \n")
            np.savetxt(dset_name_x, each_split_dset[0], delimiter=',') 

            # print(f"y: {each_split_dset[1]} \n")
            np.savetxt(dset_name_y, each_split_dset[1], delimiter=',') 
            counter += 1

        #train
        self.train(classification=classification)

    def __call__(self,X,y,with_kmeans,classification):
        self.fit(X,y,with_kmeans,classification)

    def predict(self,X, prob_score=True,classification=False):
        #Train first level
        X = [[X]]
        for each_level in range(len(self.models)):
            X = self.form_nxt_dset(self.models,each_level,X,train=False,classification=classification) if each_level <= len(self.models) else X
            print(X)
            # print(f' check X sanity {X[0][0].shape}')
            counter=1
            # print(f"self.with_kmeans: {self.with_kmeans}, self.dataset_name: {self.dataset_name}, str(each_level): {str(each_level)}")
            for each_split_dset in X:
                dset_name_x = 'dataset/'+'with_kmeans_'+ str(self.with_kmeans) +  self.dataset_name+'_x'+'level_'+str(each_level)+'learner'+'algorithm'+str(counter)+'_during_testing.csv'
                # dset_name_y = 'dataset/'+'with_kmeans_'+ str(self.with_kmeans) +  self.dataset_name+'_y'+'level_'+str(each_level)+'learner'+'algorithm'+str(counter)+'_during_testing.csv'
                np.savetxt(dset_name_x, X[0][0], delimiter=',') 

                # print(f"split: X: {self.dataset[0][0]} \n")
                # print(f"y: {self.dataset[0][1]} \n")
                # np.savetxt(dset_name_y, X[0][1], delimiter=',') 
                counter+=1
        return [[np.argmax(X[0][0], axis=1)+1]] if prob_score else X

    @staticmethod
    def create_range(range_=[]):
        encode_range,indicator = [], True
        for idx in range(len(range_)):
            start,indicator = (range_[idx], False) if indicator else (range_[idx]+1, False)
            try: 
                end = range_[idx+1]
                encode_range.append([start,end]) 
            except: 
                encode_range.append([start])
        return encode_range
        
    def check_result(self,target, preds, to_cat=False,range_=None,maxwell=False):
        """
            This helps compute the performance metrics of the out model

            target:- this are the correct outputs
            preds:- this are the model's outputs
            to_cat:- also generate the classification metrics of a regression
            problem by converting the target to range of numbers.
            range_:- This is should be a list of values where values are the range for 
            each category, this should be provided if dataset is not maxwell of desh
            or you wish to use a different range. e.g [0,8,12,21], this will be interpreted as
            [0-8] -- [9-12] -- [13-21].
            maxwell:- this is a boolean value, True means it's using maxwell's conversion
            False meaning it's using desh conversion.
        """
        if to_cat:
            if not range_:
                range_ = [0, 1500, 3000, 4500, 8000] if not maxwell else [0, 1500, 3000, 5000, 10000]
            else:
                assert type(range_) == list
                for each in range_: assert type(each) == int

            encode_range  = self.create_range(range_)
            target = self.label_target(targets=target, ranges=encode_range)
            preds = self.label_target(targets=preds, ranges=encode_range)
        # print(f'real_labes   -----------\n target --> {target}   preds --> {preds}')
        acc = accuracy_score(target,preds)
        f1_scr = f1_score(target,preds, average='weighted')
        pre = precision_score(target,preds, average='weighted')
        rec = recall_score(target,preds, average='weighted')
        return acc, f1_scr, rec, pre

    @staticmethod
    def label_target(targets, ranges):
        def checker(x, ranges):
            class_ = 1
            for each_range in ranges:
                if len(each_range) == 2 and x >= each_range[0] and x <= each_range[1]:
                    # print(f'range is --> {each_range}  label is {class_}')
                    return class_
                elif len(each_range) == 1 and x >= each_range[0]:
                    # print(f'range is --> {each_range}  label is {class_}')
                    return class_
                class_ += 1
            return 1
        return [checker(each_target,ranges) for each_target in targets.reshape(-1)]

    def split_with_kmeans(self, X, y, splitsize_max_iter=100, n_clusters=8, init='k-means++', n_init=10, max_iter=300, tol=1e-4, verbose=0, random_state=None, copy_x=True, algorithm='auto'):
        max_min = 0
        retain_preds = None
        iter_count = 0
        kmeans_instance = KMeans(n_clusters=n_clusters, init=init, n_init=n_init, max_iter=max_iter, tol=tol, verbose=verbose, random_state=random_state, copy_x=copy_x, algorithm=algorithm)
        while iter_count < splitsize_max_iter:            
            predictions = kmeans_instance.fit_predict(X=X, y=y)
            counts = np.unique(predictions, return_counts=True)[1]
            max_min,retain_preds = (np.min(counts),predictions) if np.min(counts) >= max_min else (max_min,retain_preds)
            # print(f'min min min --> {np.min(counts)}  total --> {np.sum(counts)} diffs --> {np.sum(counts)-np.min(counts)} min_max_found --> {max_min} count --> {iter_count}')
            iter_count += 1
        dataset = [[X[retain_preds==each], y[retain_preds==each]] for each in range(n_clusters)]
        #check sanity of dataset (check if dataset is not empty for all n clusted dataset, if it is fill in from existing dataset)
        ##TO-DO
        return dataset
    
    def train(self, classification=True):
        """
            function to train on the provided models.
            dataset : The datasets to run through each 
            model in the first level, Note --> if in 
            the first level there are 3 models, then, 
            3 different datasets will be expected here 
            if with_kmeans is through, but if with_kmeans 
            is False, then just one dataset will be 
            expected and that dataset will be share 
            with the three models.
        """
        assert self.dataset,"dataset is None" #check if dataset is not None
        assert type(self.dataset) is list,"dataset must be a list"
        if self.with_kmeans: assert len(self.dataset) is self.registed_level_size[0],"size of dataset should be the same with numbers of models in the registered first level"
        #Train first level
        for each_level in range(len(self.models)):
            if each_level == 0:
                #move dataset through level1
                if self.with_kmeans:
                    self.models[each_level] = [each_model.fit(X=each_dataset[0],y=each_dataset[1].reshape(-1)) for (each_model,each_dataset) in zip(self.models[each_level], self.dataset)] #pass different datasets to different models
                else:
                    # print(f'validate dataset --> {self.dataset[0][1].reshape(-1)}')
                    self.models[each_level] = [each_model.fit(self.dataset[0][0],self.dataset[0][1].reshape(-1)) for each_model in self.models[each_level]] #pass same dataset to all models
            else:
                self.models[each_level] = [each_model.fit(self.dataset[0][0],self.dataset[0][1].reshape(-1)) for each_model in self.models[each_level]] #pass same dataset to all models

            self.dataset = self.form_nxt_dset(self.models,each_level,self.dataset,train=True,classification=classification) if each_level <= len(self.models) else 0
            counter=1
            for each_split_dset in self.dataset:
                dset_name_x = 'dataset/'+'with_kmeans_'+ str(self.with_kmeans) +  self.dataset_name+'_x'+'level_'+str(each_level)+'learner'+'algorithm'+str(counter)+'_during_training.csv'
                dset_name_y = 'dataset/'+'with_kmeans_'+ str(self.with_kmeans) +  self.dataset_name+'_y'+'level_'+str(each_level)+'learner'+'algorithm'+str(counter)+'_during_training.csv'

                # print(f"counter: {counter}")
                # print(f"Dataset created after previous level {each_level}")
                np.savetxt(dset_name_x, self.dataset[0][0], delimiter=',') 

                # print(f"split: X: {self.dataset[0][0]} \n")
                # print(f"y: {self.dataset[0][1]} \n")
                np.savetxt(dset_name_y, self.dataset[0][1], delimiter=',') 
                counter += 1
                

    def form_nxt_dset(self, models=None, current_level=None,dataset=None,train=True,classification=False):
        """ Used to form next dataset """

        # assert (dataset and models and current_level),'no dataset or model or current_level provided'
        if len(dataset) > 1:
            #stack them
            new_X = None
            new_y = None
            for each in dataset:
                new_X = each[0] if new_X is None else np.concatenate((new_X,each[0]),axis=0)
                new_y = each[1] if new_y is None else np.concatenate((new_y.reshape((-1,1)),each[1].reshape((-1,1))),axis=0) if train else None
            dataset = [[new_X, new_y]] if train else [dataset]

        #infer with every model in the current level
        if classification:
            new_X = np.concatenate([each_model.predict_proba(dataset[0][0]) for each_model in models[current_level]],axis=1)
        else:
            new_X = np.concatenate([each_model.predict(dataset[0][0]).reshape((-1,1)) for each_model in models[current_level]],axis=1)
        new_y = dataset[0][1] if train else None
        # print(f'new x {new_X}')
        dataset = [[new_X,new_y]] if train else [[new_X]]
        return dataset