# Cross-Domain Sentimen Analysis Algorithm: A Guide

This repository contains a structure to apply the idea of sentiment analysis for different kinds of subjects or domains. Our code has been developed in Python 3 with some help from the following libraries, such as:
 
 * NLTK
 * Keras
 * Scikit-Learn
 * GloVe
 
 So we are going to explain how to use it and the first step is to get the data and process it.
 
 ## Preprocessing
 
First things firsts, let's get the data. We chose the using of a class to represent our data in Python. So, we has created the *Dataset* class. This class should standardize our data, because from different datasets we have different formats of data, and here we have a pattern, just the data and its labels.

### *Dataset* class

```
class Dataset:
    def __init__(self):
        self.docs = []
        self.labels = []
```

The documents are in a array and so is labels. Just that. Simple, isn't it? For that class we have some methods as well, like *add*, which insert a data in our dataset, of course. This method just receive a *Data* class as parameter and put it on out dataset. Have I not told you about the *Data* class yet? Oh, forgive me. The *Data* class has two attributes, the text data and its label, and represents a single unity of data.

We have also a second method called *get_train_test* and guess it... You're right! It divide our dataset in train and test. So you can ask me if you can get just a part of the entire dataset, yes, you can! This method receive as parameters the number of docs you want to get and the percentage of the division. Let's see an example:

```
x_train, y_train, x_test, y_test = dataset.get_train_test(0.2, 1000)
```

Here we are asking for a data sample of 1000 documents and 20% of it is for training and the rest is for test. Oh, so simple, I know you have already got it.
 
