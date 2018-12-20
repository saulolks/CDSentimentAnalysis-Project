# Cross-Domain Sentimen Analysis Algorithm: A Guide

This repository contains a structure to apply the idea of sentiment analysis for different kinds of subjects or domains. Our code has been developed in Python 3 with some help from the following libraries, such as:
 
 * NLTK
 * Keras
 * Scikit-Learn
 * GloVe
 
 The dataset we use was the following:
 
 * Amazon Reviews for Sentiment Analysis (https://www.kaggle.com/bittlingmayer/amazonreviews)
 * Movie Review Data (http://www.cs.cornell.edu/people/pabo/movie-review-data/)
 
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

#### Inserting a data in our dataset
The documents are in a array and so is labels. Just that. Simple, isn't it? For that class we have some methods as well, like *add()*, which insert a data in our dataset, of course. This method just receive a *Data* class as parameter and put it on out dataset. Have I not told you about the *Data* class yet? Oh, forgive me. The *Data* class has two attributes, the text data and its label, and represents a single unity of data. See the following example.

```
text = "I love this tutorial"
label = 1
data = Data(doc=text, label=label)
dataset.add(data)
```
Do not forget that the label is always binary, 0 for negatives and 1 for positives.

#### Getting our training and testing data
We have also a second method called *get_train_test()* and guess it... You're right! It divide our dataset in train and test. So you can ask me if you can get just a part of the entire dataset, yes, you can! This method receive as parameters the number of docs you want to get and the percentage of the division. Let's see an example:

```
x_train, y_train, x_test, y_test = dataset.get_train_test(0.2, 1000)
```

Here we are asking for a data sample of 1000 documents and 20% of it is for training and the rest is for test. Oh, so simple, I know you have already got it.

#### Saving into a CSV file
"Oh, Turorial, and if I would like to save in a CSV file?" There's no problem. The class method *save_to_csv()* generates a CSV file with all your dataset. See the example below.

```
dataset = getData()
dataset.save_to_csv()
```
This method will create a CSV file with two columns: data and label. The first one contain the tokenized texts and the second, its correspondent label. Each row contains a different data text.

```
data                                     label

this tutorial is awesome                 1
this tutorial does not explain anything  0
```

### Amazon and Movie Review preprocessing

You don't have to understand the magic that happens inside of our *py* files but it's cool see an overview about how we process the data. Ok, let's go. It will be fast.

After we get the text and its labels from the document, we separate it in tokens. So, we delete the stop words from text and lemmatize it. The data you will receive when calls the function will be divided by tokens, as a vector of words.

But you just must have the *AmazonDatasetTest.txt* and calls the function. See an example.

```
dataset = AmazonDatasetProcessing.getData()
```

It will return to you the entire Amazon dataset as a *Dataset* class. So, you will have a dataset with 400k texts and its labels. Is it too much for you? Don't worry. Use the *Dataset* class method, *get_train_test()*, and put the percentage of test and train and how much data you want, as I've already showed you. The same thing you can do with Movie Review dataset.
 
