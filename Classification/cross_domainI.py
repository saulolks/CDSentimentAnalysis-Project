#----------Cross Domain Techinique I-----
#--------Open csv file and shuffle as one big dataSet--
import os
import pandas

def prepareDataSet(datapath):
    #Shuffle
    data = pd.read_csv(datapath)
    data = data.sample(frac=1)
    X = data.iloc[:,1:6]
    Y = data['Class']
    Y = pd.get_dummies(Y)