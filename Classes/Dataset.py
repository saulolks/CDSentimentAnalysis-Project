from random import randint

class Dataset:
    def __init__(self):
        self.docs = []
        self.labels = []

    def add(self, data):
        self.docs.append(data.doc)
        self.labels.append(data.label)

    def get_train_test(self, percent, num_docs):
        num = self.docs.__len__()
        num_test = int(percent*num_docs)
        num_train = int(num_docs - num_test)

        index_train = []
        index_test = []

        while len(index_train) != num_train:
            value = randint(0, num)
            if value not in index_train:
                index_train.append(value)

        while len(index_test) != num_test:
            value = randint(0, num)
            if value not in index_train and value not in index_test:
                index_test.append(value)

        docs_train = []
        labels_train = []
        docs_test = []
        labels_test = []

        for i in index_train:
            docs_train.append(self.docs[i])
            labels_train.append(self.labels[i])

        for i in index_test:
            docs_test.append(self.docs[i])
            labels_test.append(self.labels[i])

        return docs_train, labels_train, docs_test, labels_test
