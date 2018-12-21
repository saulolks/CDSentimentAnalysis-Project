import keras
from keras import Sequential
from keras.layers import Embedding, Dropout, Conv1D, MaxPooling1D, LSTM, Dense, SeparableConv1D, Flatten
from keras_preprocessing.text import Tokenizer
from Datasets.AmazonDatasetProcessing import getData
from Preprocess.Emotional_Words import getEmotionalWords
from Preprocess.sequencing import text_to_binary
import numpy as np

# Getting the dataset
dataset = getData()
x_train, y_train, x_test, y_test = dataset.get_train_test(0.3, 50000)
print("train and test is ready")

# Getting the emotional words
dictionary = getEmotionalWords(x_train, y_train, word_precision=0.7)
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

model_conv.add(Embedding(num_of_words, 100, input_length=num_of_words))
model_conv.add(Dropout(0.2))
model_conv.add(LSTM(100))
model_conv.add(Dropout(0.2))
model_conv.add(Dense(2, activation='sigmoid', input_shape=(num_of_words, )))

model_conv.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model_conv.fit(x_train, y_train, verbose=1, epochs=3)