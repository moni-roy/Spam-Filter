import argparse
import helper as h

def read_args():
    parser = argparse.ArgumentParser(description='Classify the emails')
    parser.add_argument('-i', '--input', type=str, default="data/test.csv", help='The test data')
    parser.add_argument('-is', '--input_spam', type=str, default='data/spamProbability.csv', help='The training data of spam')
    parser.add_argument('-ih', '--input_ham', type=str, default='data/hamProbability.csv', help='The training data of ham')
    parser.add_argument('-o', '--output', type=str, default="data/result.csv", help='The result of the classification')

    args = parser.parse_args()
    return args

# first line of csv file is the total number of words in the dataset and next m lines are the word frequency
# for each word in the dataset
def read_word_frequency(file_name):
    # read text file line by line
    with open(file_name, 'r') as f:
        lines = f.readlines()
        total_word_count = int(lines[0])
        word_frequency = {}
        for line in lines[1:]:
            word, frequency = line.split(' ')
            word_frequency[word] = int(frequency)
    return total_word_count, word_frequency

# classify after reading the frequency files of ham and spam word
# calculate the probability of each word in the test set
# compare the probability of each word in the test set with the probability of each word in the training set
def classify(train_ham, train_spam, test_set):
    # read the frequency files of ham and spam word
    total_ham_word_count, ham_word_frequency = read_word_frequency(train_ham)
    total_spam_word_count, spam_word_frequency = read_word_frequency(train_spam)
 
    # total number of unique words both in ham and spam
    # get only the unique words from ham and spam
    ham_unique_words = set(ham_word_frequency.keys())
    spam_unique_words = set(spam_word_frequency.keys())
    # total number of unique words in both ham and spam
    total_word_count = ham_unique_words.union(spam_unique_words).__len__()
    
    # calculate the parameters
    # p(w|ham) = (frequency of word in ham + 1) / (total number of words in ham + total number of words)
    # p(w|spam) = (frequency of word in spam + 1) / (total number of words in spam + total number of words)
    parametrized_ham_word_frequency = {}
    parametrized_spam_word_frequency = {}
    for word, frequency in ham_word_frequency.items():
        parametrized_ham_word_frequency[word] = (frequency + 1) / (total_ham_word_count + total_word_count)
    for word, frequency in spam_word_frequency.items():
        parametrized_spam_word_frequency[word] = (frequency + 1) / (total_spam_word_count + total_word_count)

    # read the file
    test_data = h.read_csv_file(test_set)
    # predict the class of each message
    predicted_class = {}
    for message in test_data['message']:
        # clean the message
        cleaned_message = message.lower()
        # remove punctuation
        cleaned_message = cleaned_message.translate(str.maketrans('', '', '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'))
        # remove numbers
        cleaned_message = cleaned_message.translate(str.maketrans('', '', '0123456789'))
        # remove non-alphabetical characters
        cleaned_message = cleaned_message.translate(str.maketrans('', '', '!@#$%^&*()_+-=[]{};\':"|,./<>?'))
        # remove non-ascii characters
        cleaned_message = cleaned_message.encode('ascii', 'ignore').decode('ascii')

        ham_probability = 1
        spam_probability = 1
        # calculate the probability of each word in the message
        for word in cleaned_message.split(' '):
            if word in parametrized_ham_word_frequency:
                ham_probability *= parametrized_ham_word_frequency[word]
            else:
                ham_probability *= 1 / (total_ham_word_count + total_word_count)
            if word in parametrized_spam_word_frequency:
                spam_probability *= parametrized_spam_word_frequency[word]
            else:
                spam_probability *= 1 / (total_spam_word_count + total_word_count)

        # compare the probability of each word in the message with the probability of each word in the training set
        if ham_probability > spam_probability:
            predicted_class[message] = 'ham'
        else:
            predicted_class[message] = 'spam'
    
    # save the result to the output file as key, value pair of message and its classification
    with open(args.output, 'w') as f:
        f.write('label, message\n')
        for key, value in predicted_class.items():
            f.write(value + ', ' + key + '\n')
    
if __name__ == '__main__':
    args = read_args()
    classify(args.input_ham, args.input_spam, args.input)
