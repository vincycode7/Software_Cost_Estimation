class trainer:
    def __init__(self,levels=2, level_model=None, with_kmeans=True):
        """ 
            This is the stack ensemble trainer that trains on different 
            base learners.

            levels :- Specifies how many levels there are in the training 
            process, where the first level is for base learner and other
            levels is for meta learner.
            
            Example1 levels = 2 : this means 1 level for base learners to learn and 1 level
            for meta learners.

            Example2 levels = 7 : this means 1 level for base learners to learn and 6 level
            for meta learners.


            level_model :- This is where every model(in a list or tuple) is specified for each 
            level and each model-list is stored in an outer list.

            Example 1 level = 2, level_model = [[knn, svm, dt], [svm]]
            Example 1 level = 3, level_model = [[knn, svm, dt], [svm,knn],[svm]]

            note :- the model in the last level should be one else the first one is picked.
        """
        self.levels = levels
        self.models = level_model
        self.register_level_size = {level_index:len(level_model[level_index]) for level_index in range(self.models)}