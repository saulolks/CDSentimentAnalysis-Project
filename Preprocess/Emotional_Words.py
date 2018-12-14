def getDictionary(data, dict_size):
    vocabulary = {}
    for document in data:
        for word in document:
            if word in vocabulary:
                j = vocabulary[word]
                j = j + 1
                vocabulary[word] = j
            else:
                vocabulary[word] = 1

    dictionary = []
    for word in vocabulary:
        dictionary.append([word, vocabulary[word]])

    dictionary.sort(key=lambda x: x[1], reverse=True)
    return dictionary[:dict_size]


# verify if a word has a tendency to appear in a kind of label
# getting the percent of its occurence in positive and negative
# documents. if the percentage is near to 0.5, it's a neutral word.
# the limit of percentage to define is passed as a parameter.
def identifyEmotional(word_occurence, percentage):
    size = len(word_occurence)
    emotional_words = []

    for i in range(size):
        neg = word_occurence[i][0]
        pos = word_occurence[i][1]

<<<<<<< HEAD
        total = neg + pos
        neg = neg / total
        pos = pos / total
=======
        #total = neg + pos
        neg = neg / size
        pos = pos / size
        print(neg, pos)
>>>>>>> master

        if neg >= percentage:
            emotional_words.append([0, round(neg,2), round(pos,2)])
        elif pos >= percentage:
            emotional_words.append([1, round(neg,2), round(pos,2)])
        else:
            emotional_words.append([-1, round(neg,2), round(pos,2)])

    return emotional_words


# this function produces a list of lists containing a 2-dimensional vector
# for each word in dictionary. the vector V represents V[0] the percentile
# of appearance of that word in negative documents, and V[1], in positive.
<<<<<<< HEAD
def getEmotionalWords(data, label, dict_size=-1, word_precision=0.7):
=======
def getEmotionalWords(data, label, dict_size=-1, word_precision=0.2):
>>>>>>> master
    size = len(data)

    if dict_size < 0:
        dict_size = int(len(data) / 4)

    dictionary = getDictionary(data, dict_size)

    word_occurence = []

    for word in dictionary:
        wordVec = [0, 0]
        for i in range(size):
            if word[0] in data[i]:
                wordVec[label[i]] = wordVec[label[i]] + 1
        word_occurence.append(wordVec)
    emotional_words = identifyEmotional(word_occurence, word_precision)

    for i in range(len(emotional_words)):
        if emotional_words[i][0] != -1:
            print(dictionary[i][0], emotional_words[i])
