from random import randint

import xlrd
import xlwt
from xlutils.copy import copy

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
            value = randint(0, num-1)
            if value not in index_train:
                index_train.append(value)

        while len(index_test) != num_test:
            value = randint(0, num-1)
            if value not in index_train and value not in index_test:
                index_test.append(value)

        docs_train = []
        labels_train = []
        docs_test = []
        labels_test = []

        '''
        arq = open('Files/datasets/amazontrain.txt', 'w')
        for i in index_train:
            arq.write("%d " %i)
        arq.close()

        arq = open('Files/datasets/amazontest.txt', 'w')
        for i in index_test:
            arq.write("%d " %i)
        arq.close()
        '''

        for i in index_train:
            docs_train.append(self.docs[i])
            labels_train.append(self.labels[i])

        for i in index_test:
            docs_test.append(self.docs[i])
            labels_test.append(self.labels[i])

        return docs_train, labels_train, docs_test, labels_test

    @staticmethod
    def criar_arquivo():
        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet("dataset", True)
        worksheet.write(0, 0, 'data')
        worksheet.write(0, 1, 'label')
        workbook.save("dataset.xls")

    def save_to_csv(self):
        self.criar_arquivo()
        workbook = xlrd.open_workbook("dataset.xls")
        worksheet = workbook.sheet_by_index(0)

        wb = copy(workbook)
        linha = worksheet.nrows
        sheet = wb.get_sheet(0)

        for i in range(len(self.docs)):
            text = ""
            for word in self.docs[i]:
                text = text + " " + word

            sheet.write(linha+i, 0, text)
            sheet.write(linha+i, 1, self.labels[i])

        try:
            wb.save("dataset.xls")
        except IOError:
            wb.save("dataset.xls")