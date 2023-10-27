import numpy
from keras.models import load_model
from Feature_Extraction import Main
import decimal
import joblib
import os

path = os.getcwd()

def process_text(s):
    # Check string to see if they are a punctuation
    nopunc = [char for char in s if char not in string.punctuation]

    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)

    # Convert string to lowercase and remove stopwords
    clean_string = [word for word in nopunc.split()]
    return clean_string

def check_url(url):
    data = Main(url)
    print(data)
    result = list()
    for val in data.values():
        if (isinstance(val, decimal.Decimal)):
            val = float(val)
        result.append(val)
    X_new = numpy.array(result)
    X_new = numpy.expand_dims(X_new, axis=0)
    clf = joblib.load(os.path.join(path, "model_pickle_RF"))
    y_rf = clf.predict(X_new)
    if (y_rf[0] == 1):
        print("Website is malicious!!")
        return "malicious"
    else:
        print("Website is safe!!")
        return "safe"

# if __name__ == '__main__':
#     url = "dantri.com"
#     check_url(url)
