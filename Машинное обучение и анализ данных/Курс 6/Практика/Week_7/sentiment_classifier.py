__author__ = 'xead'
from sklearn.externals import joblib


class SentimentClassifier(object):
    def __init__(self):
        self.model = joblib.load("C:\Users\dim\Desktop/Week_7/pipeline_2.pkl")
        self.classes_dict = {0: "negative", 1: "positive", -1: "prediction error"}


    def predict_text(self, text):
        try:
            prediction=self.model.predict([text])
            return prediction[0]
        except:
            print "prediction error"
            return -1

    def get_prediction_message(self, text):
        prediction = self.predict_text(text)
        return self.classes_dict[prediction]