import argparse
import helper as h

def read_args():
    parser = argparse.ArgumentParser(description='Add new input to training set')
    parser.add_argument('-is', '--input_spam', type=str, default='data/spamProbability.csv', help='input spam probability file')
    parser.add_argument('-ih', '--input_ham', type=str, default='data/hamProbability.csv', help='input ham probability file')
    parser.add_argument('-i', '--input', type=str, default='data/input.csv', help='input file')
    return parser.parse_args() 

# read frequency files for ham and spam
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

# read frequency files for ham and spam, add new input files to frequency files
# and write to the previous frequency files
def addToTraining(ham, spam, input_file):
    # read frequency files for ham and spam
    total_word_count_ham, word_frequency_ham = read_word_frequency(ham)
    total_word_count_spam, word_frequency_spam = read_word_frequency(spam)
    
    # read new input csv file line by line
    data = h.read_csv_file(input_file)
    # clean data
    data = h.clean_data(data)
    
    # line by line pd dataframe 
    for index, row in data.iterrows():
        # get the label and text from the input file
        label = row[0]
        text = row[1]
        # split text into words
        words = text.split()
        # update frequency files for ham and spam
        if label == 'ham':
            for word in words:
                if word in word_frequency_ham:
                    word_frequency_ham[word] += 1
                else:
                    word_frequency_ham[word] = 1
                total_word_count_ham += 1
        else:
            for word in words:
                if word in word_frequency_spam:
                    word_frequency_spam[word] += 1
                else:
                    word_frequency_spam[word] = 1
                total_word_count_spam += 1
                
    # write to the previous frequency files
    with open(ham, 'w') as f:
        f.write(str(total_word_count_ham) + '\n')
        for word, frequency in word_frequency_ham.items():
            f.write(word + ' ' + str(frequency) + '\n')
    with open(spam, 'w') as f:
        f.write(str(total_word_count_spam) + '\n')
        for word, frequency in word_frequency_spam.items():
            f.write(word + ' ' + str(frequency) + '\n')

if __name__ == '__main__':
    args = read_args()
    addToTraining(args.input_ham, args.input_spam, args.input)
    print('Done!')
    exit(0)
    