from Datasets.RottenDatasetPreprocessing import getData
from Preprocess.Emotional_Words import getEmotionalWords
from Preprocess.sequencing import text_to_tfidf

dataset = getData()
print("dataset is ready")
print(len(dataset.docs))
x_train, y_train, x_test, y_test = dataset.get_train_test(0.3, 5000)
print("train and test is ready")
dictionary = getEmotionalWords(x_train, y_train, word_precision=0.8)
print("emotional words as well")
print(dictionary)