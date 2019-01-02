import pickle

from Classes.Data import Data
from Classes.Dataset import Dataset
from Preprocess.preProcessing import to_process

def genAmazonData():
    dataset = Dataset()
    arq = open('Datasets/AmazonDatasetTest.txt', 'r', encoding='utf-8')
    i = 0
    while True:
        try:
            line = arq.readline()
            if line == "":
                break
            print(i)
            i = i+1

            # Reading labels and data
            label = int(line[9])
            label = 0 if label == 1 else 1
            text = line[11:len(line)-1]

            # Tokenizing and lemmatizing
            text = to_process(text)
            
            data = Data(doc=text,label=label)
            dataset.add(data)
        except EOFError:
            break

    with open('amazon_dataset', 'wb') as fp:
        pickle.dump(dataset, fp)

    return dataset

def getData():
    amazondataset = Dataset()
    try:
        with open('Datasets/amazon_dataset', 'rb') as fp:
            amazondataset = pickle.load(fp)
    except:
        amazondataset = genAmazonData()
    
    return amazondataset

if __name__ == '__main__':
    main()


