from os import write
import pandas as pd
import argparse
import helper as h

# read arguments
def read_arguments():
    parser = argparse.ArgumentParser(description='Train a model')
    parser.add_argument('-i', '--input', type=str, default='data/spam.csv', help='Input file')
    parser.add_argument('-os', '--outputSpam', type=str, default='data/spamProbability.csv', help='Spam probability output file')
    parser.add_argument('-oh', '--outputHam', type=str, default='data/hamProbability.csv', help='Ham probability output file')

    args = parser.parse_args()
    return args

# build word frequency for each word in the each label ham and spam with key as word and value as frequency
# add the total word count for each label at the begging the csv file
# add the word frequency for each label at the end of the csv file
def build_word_frequency_with_total(data, args):
    # split data into ham and spam
    spam = data[data['label'] == 'spam']
    ham = data[data['label'] == 'ham']


    # concatenate all messages for each label
    spam_all_messages = spam['message'].str.cat(sep=' ')
    ham_all_messages = ham['message'].str.cat(sep=' ')

    # total word number for each label
    spam_total_word_count = len(spam_all_messages.split())
    ham_total_word_count = len(ham_all_messages.split())

    # build word frequency for each word in the each label ham and spam with key as word and value as frequency 
    # with key as word and value as frequency
    spam_word_frequency = {}
    ham_word_frequency = {}

    # build word frequency for each word in the each label ham and spam with key as word and value as frequency
    # with key as word and value as frequency
    for word in spam_all_messages.split():
        if word in spam_word_frequency:
            spam_word_frequency[word] += 1
        else:
            spam_word_frequency[word] = 1

    for word in ham_all_messages.split():
        if word in ham_word_frequency:
            ham_word_frequency[word] += 1
        else:
            ham_word_frequency[word] = 1

    # save word frequency for each label to a text file
    spam_word_frequency_file = open(args.outputSpam, 'w')
    ham_word_frequency_file = open(args.outputHam, 'w')
    
    # add the total word count for each label at the begging the csv file
    spam_word_frequency_file.write(str(spam_total_word_count) + '\n')
    ham_word_frequency_file.write(str(ham_total_word_count) + '\n')


    # add the word frequency for each label at the end of the csv file
    for word in spam_word_frequency:
        spam_word_frequency_file.write(word + ' ' + str(spam_word_frequency[word]) + '\n')
    
    for word in ham_word_frequency:
        ham_word_frequency_file.write(word + ' ' + str(ham_word_frequency[word]) + '\n')
    
    spam_word_frequency_file.close()
    ham_word_frequency_file.close()
    
def main():
    # read arguments
    args = read_arguments()

    # read csv file
    data = h.read_csv_file(args.input)

    # build word frequency
    build_word_frequency_with_total(data, args)

if __name__ == "__main__":
    main()
