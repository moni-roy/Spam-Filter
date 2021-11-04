# Spam-Filter

A project for CS 682 - Artificial Intelligence

## Purpose

The purpose of this assignment is to provide a multi-executable programming experience with a discriminatory algorithm that can make decisions using Artificial Intelligence. You should be able to utilize probability in order to classify using a Naive Bayes Classifier.

## Task

Please write a program to parse an existing dataset on real-world SMS messages. (note: since these data come from real-world interactions, these messages may use language which I would never use in class and that violates professional conversational norms. If that is likely to trigger a negative reaction, please do not read the messages themselves. However, I feel that it is important to work with real-world data wherever possible).

You will need to write two programs:

1.  `training -i <spam.csv file> -os <output spam probability file> -oh <output ham probability file>`

    Trains dataset from .csv file and save to new file. Each line of the .csv file has at least two fields, separated by a comma:

        1. <spam|ham> ham if it is a legitimate SMS, spam if not
        2. "..." the SMS message

    You will need to output two probability files (one for ham, one for spam):

        <count of the total number of words (n)>
        m lines, one for each word
        <word> <number of word occurrences>

2.  `classify -i <testing dataset .csv file> -is <spam probability file> -ih <ham probability file> -o <classification output filename>`

    Classifies new data from training file and testing .csv file (same format as above, specified on the command-line)

    You will need to output one classification file:

        m lines, one for each SMS in the testing dataset (in the same order as the testing set is in <spam/ham> (the classification of the SMS)

### Graduate Student Extra Assignment

Please also write a program to add new data (in a .csv file) to the existing training database.

`addtotraining -is <input spam probability file> -ih <input ham probability file> -s "<string>"`
