from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

class ProcessData:
    def __init__(self, dataset):
        self.dataset = dataset

    def processData(self):
        le = LabelEncoder()
        zomato_edit = self.dataset.copy()
        zomato_edit['Price range'] = le.fit_transform(zomato_edit['Price range'])
        return zomato_edit

    def splitData(self):
        X = self.dataset.drop(['Price range'], axis=1).to_numpy()
        y = self.dataset['Price range'].to_numpy()

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

        return X_train, X_test, y_train, y_test
