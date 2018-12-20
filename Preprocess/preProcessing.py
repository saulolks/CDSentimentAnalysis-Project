
import nltk
from nltk import WordNetLemmatizer
from keras.preprocessing.text import text_to_word_sequence

lemmatizer = WordNetLemmatizer()

def to_process(text):
    # Reading stop-words
    arq = open('Preprocess/sw.txt', 'r')
    stopWords = arq.read()

    # Tokenizing and lemmatizing the documents
    stopWords = text_to_word_sequence(stopWords)
    tokens = text_to_word_sequence(text)
    text = [lemmatizer.lemmatize(word) for word in tokens]

    result = []

    for word in text:
        if word not in stopWords:
            result.append(word)

    return result
