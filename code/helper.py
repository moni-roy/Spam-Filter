import pandas as pd

def clean_data(data):
    # lowercase
    data['message'] = data['message'].str.lower()
    # clean punctuation
    data['message'] = data['message'].str.replace('[^\w\s]','',regex=True)
    # clean numbers
    data['message'] = data['message'].str.replace('\d+','',regex=True)
    # remove multiple spaces
    data['message'] = data['message'].str.replace('\s+', ' ', regex=True)
    # remove non-ascii characters
    data['message'] = data['message'].str.replace('[^\x00-\x7F]+', '', regex=True)
    # remove not alphabetic characters and spaces
    data['message'] = data['message'].str.replace('[^a-zA-Z\s]', '', regex=True)
    # remove single characters
    data['message'] = data['message'].str.replace('\s+[a-zA-Z]\s+', ' ', regex=True)
    # remove hyperlinks
    data['message'] = data['message'].str.replace('http\S+', '', regex=True)
    return data

# read a csv file keep only first two columns and rename them as 'label' and 'message'
def read_csv_file(file_name):
    print('Reading csv file: ' + file_name)
    data = pd.read_csv(file_name, usecols=[0,1])
    data.columns = ['label', 'message']
    return data