#----------Cross Domain Techinique I-----
#--------Open csv file and shuffle as one big dataSet--

#Imports
import pandas as pd
from sklearn.model_selection import KFold
import Classification.MLP as mlp

"""
Function reads csv file and splits each individual features from it's class.
X -> Contains features for each individual
Y -> Contains the classes of each individual
"""
def prepareDataSet(datapath):
    #Shuffle
    data = pd.read_csv(datapath)
    data = data.sample(frac=1)

    #Variate this according TO THE DATA <<<<<<<<< IMPORTANT
    X = data.iloc[:,1:6]
    Y = data['Class']
    Y = pd.get_dummies(Y)
    return X,Y
"""
Function to call the Classifiers (MLP/ CNN)
to classify given data (Split into test and train)
"""
def call_classifiers(x_train, y_train, x_test, y_test):
    mlp.mlp(x_train, y_train, x_test, y_test)
    #Call CNN LATER

"""
common 10-fold for CDI
Splits data into 10 folds to train and test in cross-validation
"""
def kfold(X,Y):
    kf = KFold(n_splits=10, shuffle=False)
    for train_index, test_index in kf.split(X):
        x_train, x_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = Y.iloc[train_index], Y.iloc[test_index]
        call_classifiers(x_train, y_train, x_test, y_test)
def cd1():
    datapath = ""  #INSERT CSV FILE HERE
    X,Y = prepareDataSet(datapath)
    kfold(X,Y)