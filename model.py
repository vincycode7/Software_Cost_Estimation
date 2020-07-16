from sklearn.cluster import KMeans

class StackEnsemble:
    def __init__(self,levels=2, level_model=None, with_kmeans=True):
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
                    #level_model[-1] = [level_model[-1][0]] #pick the first model in the last level
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
                ValueError('No model passed')

        self.models = level_model
        self.registed_level_size = {level_index:len(self.models[level_index]) for level_index in range(len(self.models))}
        self._dataset = None
        self.with_kmeans = None

    # @property
    # def dataset(self):
    #     return self._dataset
    
    # @dataset.setter
    # def dataset(self, value=None):
    #     if value == None:
    #         return value

    #     if self.with_kmeans:
    #         #merge all dataset and split them into n base learners
    #         pass
    #     else:
    #         if len(value) == self.register_level_size[0]:
    #             self._dataset = value
    #         elif len(value) > self.register_level_size[0]:
    #             """
    #                 here the n-base dataset will be selected and the 
    #                 remaining will be added to the n-base selected
    #             """
    #             pass #Not implemented yet
    #         else:
    #             """
    #                 here all the dataset will be concated into 1
    #                 and splitted to n-base.
    #             """
    #             pass #Not implemented y


    def fit(self, X, y, with_kmeans=True):
        self.with_kmeans = with_kmeans
        #split with kmeans or not
        self.dataset = self.split_with_kmeans(X,y,len(self.models[0])) #returns list of n dataset
        #train
        self.train()

    def __call__(self,X,y,with_kmeans):
        self.fit(X,y,with_kmeans)

    def predict(self,value):
        return 0

    def check_result(self,target, preds, to_cat=True):
        """
            This helps compute the performance metrics of the out model

            target:- this are the correct outputs
            preds:- this are the model's outputs
            to_cat:- also generate the classification metrics of a regression
            problem by converting the target to range of numbers.
        """
        NotImplementedError

    def split_with_kmeans(self, X, y, n_clusters=8, init='k-means++', n_init=10, max_iter=300, tol=1e-4, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=None, algorithm='auto'):
        kmeans_instance = KMeans(n_clusters=n_clusters, init=init, n_init=n_init, max_iter=max_iter, tol=tol, precompute_distances=precompute_distances, verbose=verbose, random_state=random_state, copy_x=copy_x, n_jobs=n_jobs, algorithm=algorithm)
        predictions = kmeans_instance.fit_predict(X=X, y=y)
        dataset = [[X[predictions==each], y[predictions==each]] for each in range(n_clusters)]

        #check sanity of dataset (check if dataset is not empty for all n clusted dataset, if it is fill in from existing dataset)
        #TODO
        return dataset
    
    def train(self):
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
        assert not self.dataset,"dataset is None" #check if dataset is not None
        assert type(self.dataset) is list,"dataset must be a list"
        if self.with_kmeans: assert len(self.dataset) is self.registed_level_size[0],"size of dataset should be the same with numbers of models in the registered first level"
        #Train first level
        pass