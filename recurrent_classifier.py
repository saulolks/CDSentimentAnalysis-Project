import keras
from keras import Sequential
from keras.layers import Embedding, Dropout, Conv1D, MaxPooling1D, LSTM, Dense, SeparableConv1D, Flatten, \
    SeparableConv2D, Conv2D
from keras_preprocessing.text import Tokenizer
from Datasets.AmazonDatasetProcessing import getData
from Preprocess.Emotional_Words import getEmotionalWords
from Preprocess.sequencing import text_to_binary
import numpy as np

# Getting the dataset
dataset = getData()
x_train, y_train, x_test, y_test = dataset.get_train_test(0.3, 10000)
print("train and test is ready")

# Getting the emotional words
dictionary = getEmotionalWords(x_train, y_train, word_precision=0.6, pos_filter='parcial')
print("emotional words as well")

y_train = np.array(y_train)
y_train = keras.utils.to_categorical(y_train, 2)

data_size = len(x_train)
num_of_words = len(dictionary)
print("vocabulary size = ", num_of_words)
print("data size = ", len(x_train))

# Getting the binary vector
x_train = text_to_binary(x_train, dictionary)
x_train = np.array(x_train)

# Convolutional Model
model_conv = Sequential()

model_conv.add(Embedding(num_of_words, 128))
model_conv.add(LSTM(600))
model_conv.add(Conv2D(filters=64, kernel_size=(5, 600)))
model_conv.add(Dropout(0.5))
model_conv.add(MaxPooling1D())

model_conv.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model_conv.fit(x_train, y_train, verbose=1, epochs=3)
