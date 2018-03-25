# -*- coding: utf-8 -*-
__author__ = 'VladimirSveshnikov'
from encoder import Model

model=Model()

class SentimentClassifier(object):
    def __init__(self):
        self.model = model
        self.classes_dict = {0: "negative", 1: "positive", -1: "prediction error"}

    @staticmethod
    def get_probability_words(probability):
        if probability < 0.55:
            return "neutral or uncertain"
        if probability < 0.7:
            return "probably"
        if probability > 0.95:
            return "certain"
        else:
            return ""

    def predict_text(self, text):
        try:
            text_features = model.transform([text])
            print(text_features[0, 2388] )
            return 0 if text_features[0, 2388] <= 0 else 1,\
                text_features[0, 2388]
        except:
            print ("prediction error")
            return -1, 0.8

    def predict_list(self, list_of_texts):
        try:
            text_features = model.transform(list_of_texts)
            predict = 0
            predict_arr = []
            for i in range(len(list_of_texts)):
                predict += text_features[i, 2388]
                predict_arr.append(text_features[i, 2388])
            return 0 if predict / len(list_of_texts) <= 0 else 1,\
                predict / len(list_of_texts)
        except:
            print ('prediction error')
            return None

    def get_prediction_message(self, text):
        prediction = self.predict_text(text)
        class_prediction = prediction[0]
        prediction_probability = prediction[1]
        return [self.get_probability_words(prediction_probability) + " " + self.classes_dict[class_prediction], class_prediction]