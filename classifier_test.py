# coding: utf-8
__author__ = 'VladimirSveshnikov'

from sentiment_classifier import SentimentClassifier

clf = SentimentClassifier()

pred = clf.get_prediction_message("This is an excellent bank, just wonderful")

print (pred)