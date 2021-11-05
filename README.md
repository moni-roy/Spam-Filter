# Spam-Filter

A project for CS 682 - Artificial Intelligence

## Purpose

The purpose of this assignment is to provide a multi-executable programming experience with a discriminatory algorithm that can make decisions using Artificial Intelligence. You should be able to utilize probability in order to classify using a Naive Bayes Classifier.

## Task

Please write a program to parse an existing dataset on real-world SMS messages. (note: since these data come from real-world interactions, these messages may use language which I would never use in class and that violates professional conversational norms. If that is likely to trigger a negative reaction, please do not read the messages themselves. However, I feel that it is important to work with real-world data wherever possible).

You will need to write two programs:

1.  `training -i <spam.csv file> -os <output spam probability file> -oh <output ham probability file>`

    Trains dataset from .csv file and save to new file. Each line of the .csv file has at least two fields, separated by a comma:

    ```text
    1. <spam|ham> ham if it is a legitimate SMS, spam if not
    2. "..." the SMS message
    ```

    You will need to output two probability files (one for ham, one for spam):

    ```text
    <count of the total number of words (n)>
    m lines, one for each word
    <word> <number of word occurrences>
    ```

2.  `classify -i <testing dataset .csv file> -is <spam probability file> -ih <ham probability file> -o <classification output filename>`

    Classifies new data from training file and testing .csv file (same format as above, specified on the command-line)

    You will need to output one classification file:

    ```text
    m lines, one for each SMS in the testing dataset
    (in the same order as the testing set is in <spam/ham>)
    (the classification of the SMS)
    ```

### Graduate Student Extra Assignment

Please also write a program to add new data (in a .csv file) to the existing training database.

`addtotraining -is <input spam probability file> -ih <input ham probability file> -s "<string>"`

## Solution/Algorithms

Naive Bayes Classifier is used to calculate the probability of the spam/hum messages.

### Naive Bayes Classifier

Naive Bayes classifiers are highly scalable, requiring a number of parameters linear in the number of variables (features/predictors) in a learning problem. Maximum-likelihood training can be done by evaluating a closed-form expression,  which takes linear time, rather than by expensive iterative approximation as used for many other types of classifiers.

#### Equation:

```math
P(w|c) = (C(w, c) + 1) / (C(c) + |V|)

where,
P(w|c) = the probability of a word belongs to given class c (ham/spam)
C(w, c) =  the frequency of the word in the given class c
C(c) = total number of words in the given class
|V| = number of the unique vocabulary in the dataset.
```

## Pre-requisites and Environment Settings

- Python >= 3.8
- Pandas

## Run Command

```text
<create a virtual environment>
python3 -m venv spamfilter

<activate the virtual environment>
source spamfilter/bin/activate

<install the requirement>
python3 -m pip install -r requirements.txt

<run the training code>
python3 code/training.py -i <spam.csv file> -os <output spam probability file> -oh <output ham probability file>`

<classify the test set>
python3 code/classify.py -i <testing dataset .csv file> -is <spam probability file> -ih <ham probability file> -o <classification output filename>

<add new training to training set>
python3 code/addtotraining.py -is <input spam probability file> -ih <input ham probability file> -s <new training set file>

```

Some notes,

- Creating and activating virtual environment are optional steps.
- Training input file should have level in the first row, otherwise first rows will be excluded from data.
- Same condition applicable for addToTraining. It should be a file and same structure as training file.
