import pickle

import nltk
from nltk import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def to_process(vocabulary, num_of_words):
    ## Reading stop-words
    arq = open('stopwords.txt', 'r')
    stopWords = arq.read()
    stopWords = nltk.word_tokenize(stopWords)

    ## Generating a vector of 2-dimensional vectors that will
    ## bin the word and its frequence

    filteredVocabulary = []
    for w in vocabulary:
        if w not in stopWords:
            filteredVocabulary.append([w, vocabulary[w]])

    ## Sorting by frequence and getting the n-firsts words
    ## from vocabulary
    filteredVocabulary.sort(key=lambda x: x[1], reverse=True)
    filteredVocabulary = filteredVocabulary[0:num_of_words]
    arq.close()
    print(filteredVocabulary)
    return filteredVocabulary

def generate_dictionary(docs,  num_of_words):
    dictionary = {}
    for doc in docs:
        text = nltk.word_tokenize(doc)
        text = [lemmatizer.lemmatize(word) for word in text]
        text = [word.lower() for word in text if word.isalpha()]
        
        for word in text:
            if word in dictionary:
                j = dictionary[word]
                j += 1
                dictionary[word] = j
            else:
                dictionary[word] = 1
    
    dictionary = to_process(dictionary, num_of_words)
    return dictionary

def data_to_bow(docs, num_of_words):
    dictionary = generate_dictionary(docs, num_of_words)
    bow = []
    for doc in docs:
        textline = []

        text = nltk.word_tokenize(doc)
        text = [lemmatizer.lemmatize(word) for word in text]
        text = [word.lower() for word in text if word.isalpha()]

        for word in dictionary:
            if word[0] in text:
                textline.append(1)
            else:
                textline.append(0)

        bow.append(textline)

    return bow