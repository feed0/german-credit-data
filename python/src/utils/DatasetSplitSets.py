class DatasetSplitSets:
    def __init__(self, train, test, y_train, y_test):
        self.X_train = train
        self.X_test  = test
        self.y_train = y_train
        self.y_test  = y_test