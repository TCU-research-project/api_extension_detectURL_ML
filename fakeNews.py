from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
import string
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

async def checkNews(news):
    # Đường dẫn và tên file model
    model_filename = "random_forest_model.pkl"

    # Load model từ file
    loaded_model = await joblib.load((os.path.join(path, model_filename)))
    data = [
        "Cuộc điều tra mới nhất đã tiết lộ rằng một nhóm các nhà nghiên cứu hàng đầu đã phát hiện ra một phương pháp mới để ngăn chặn ung thư. Phương pháp này cho phép loại bỏ hoàn toàn tác nhân gây ung thư khỏi cơ thể mà không gây tác động đến tế bào khỏe mạnh. Điều này có thể là một bước đột phá trong cuộc chiến chống ung thư và mang lại hy vọng cho hàng triệu người trên thế giới."]
    
    # Sử dụng model để dự đoán
    predictions = loaded_model.predict(data)[0]
    return predictions
