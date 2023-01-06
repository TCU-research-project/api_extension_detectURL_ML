import numpy
from keras.models import load_model
from app.Feature_Extraction import Main
import decimal
import joblib
import os

path = os.getcwd()

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
    clf = joblib.load(os.path.join(path, "app", "model_pickle_RF"))
    y_rf = clf.predict(X_new)
    if (y_rf[0] == 1):
        print("Website is malicious!!")
        return 1
    else:
        print("Website is safe!!")
        return 0

# if __name__ == '__main__':
#     url = "dantri.com"
#     check_url(url)
