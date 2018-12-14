import pickle

from keras_preprocessing.text import Tokenizer
from Classes.Data import Data
from Classes.Dataset import Dataset
from Preprocess.preProcessing import to_process
from Preprocess.Emotional_Words import getEmotionalWords


def genAmazonData():
    dataset = Dataset()
    arq = open('AmazonDatasetTest.txt', 'r', encoding='utf-8')
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

def main():
    with open('amazon_dataset', 'rb') as fp:
        amazondataset = pickle.load(fp)

    x_train, y_train, x_test, y_test = amazondataset.get_train_test(0.2, 1000)

    getEmotionalWords(x_train, y_train)

if __name__ == '__main__':
    main()



