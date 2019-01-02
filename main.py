import xlrd
import xlwt
from xlutils.copy import copy
from Datasets.AmazonDatasetProcessing import getData
from Preprocess.Emotional_Words import getEmotionalWords, getDictionary
from Preprocess.sequencing import text_to_binary

#############################################################################

dataset = getData()
print("dataset is ready")
print(len(dataset.docs))

x_train, y_train, x_test, y_test = dataset.get_train_test(0.2, 1000)
print("train and test is ready")
print(x_train.__len__())

##############################################################################

dictionary = getDictionary(x_train, 2000)
# dictionary = getEmotionalWords(x_train, y_train, word_precision=0.6)
print("dictionary as well")
print(dictionary.__len__())

matrix = text_to_binary(x_train, dictionary)
print("sequencing is ok")

###############################################################################

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet("amazon50k-binary-noEW", True)
worksheet.write(0, 0, '50k')
worksheet.write(0, 1, 'binary-noEW')
workbook.save("Files/amazon50k-binary-noEW.xls")

workbook = xlrd.open_workbook("Files/amazon50k-binary-noEW.xls")
worksheet = workbook.sheet_by_index(0)

wb = copy(workbook)
linha = worksheet.nrows
sheet = wb.get_sheet(0)

for i in range(len(matrix)-1):
    for j in range(len(matrix[0])-1):
        print(i, j)
        sheet.write(linha+i, j, matrix[i][j])

try:
    wb.save("Files/amazon50k-binary-noEW.xls")
except IOError:
    wb.save("Files/amazon50k-binary-noEW.xls")