import numpy as np
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

def load_data():
    iris = datasets.load_iris()
    X = iris.data[:, :2]  # On prend 2 features
    y = iris.target
    return train_test_split(X, y, test_size=0.3, random_state=42)

def train_svm(X_train, y_train, kernel="linear", C=1.0):
    model = svm.SVC(kernel=kernel, C=C)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy
