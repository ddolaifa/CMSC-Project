from sklearn.model_selection import cross_val_score
import numpy as np
from sklearn.linear_model import SGDClassifier

class TrainData:
    def __init__(self):
        pass

    def trainData(self, X_train, X_test, y_train, y_test):
        model = SGDClassifier()
        accuracy_scores = cross_val_score(model, X_train, y_train, scoring='accuracy', n_jobs=-1)
        f1_scores = cross_val_score(model, X_train, y_train, scoring='f1_weighted', n_jobs=-1)

        print(np.mean(accuracy_scores))
        print(np.mean(f1_scores))