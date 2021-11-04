# from nltk.corpus import stopwords
import pandas as pd

def cleaning_data(data):
    # lowercase
    data['message'] = data['message'].str.lower()
    # clean punctuation
    data['message'] = data['message'].str.replace('[^\w\s]','')
    # clean numbers
    data['message'] = data['message'].str.replace('\d+','')
    # remove multiple spaces
    data['message'] = data['message'].str.replace('\s+', ' ')
    # remove non-ascii characters
    data['message'] = data['message'].str.replace('[^\x00-\x7F]+', '')
    # remove not alphabetic characters and spaces
    data['message'] = data['message'].str.replace('[^a-zA-Z\s]', '')
    # remove english stop words using library
    # stop_words = set(stopwords.words('english'))
    # data['message'] = data['message'].apply(lambda x: ' '.join(x for x in x.split() if x not in stop_words))
    # remove single characters
    data['message'] = data['message'].str.replace('\s+[a-zA-Z]\s+', ' ')
    return data

# read a csv file keep only first two columns and rename them as 'label' and 'message'
def read_csv_file(file_name):
    print('Reading csv file: ' + file_name)
    data = pd.read_csv(file_name, usecols=[0,1])
    data.columns = ['label', 'message']
    data = cleaning_data(data)
    print(data.head())
    return data