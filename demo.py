__author__ = 'VladimirSveshnikov'
from sentiment_classifier import SentimentClassifier
from codecs import open
import time
from flask import Flask, render_template, request
app = Flask(__name__)

print ("Preparing classifier")
start_time = time.time()
classifier = SentimentClassifier()
print ("Classifier is ready")
print (time.time() - start_time, "seconds")

@app.route("/sentiment-demo", methods=["POST", "GET"])
def index_page(text="", prediction_message=""):
    if request.method == "POST":
        text = request.form["text"]
        logfile = open("ydf_demo_logs.txt", "a", "utf-8")
        print (text)
        print ("<response>", file=logfile)
        print (text, file=logfile)
        prediction_message, score = classifier.get_prediction_message(text)
        print (prediction_message, ', ', score)
        print (prediction_message, file=logfile)
        print ("</response>", file=logfile)
        logfile.close()
		
    return render_template('hello.html', text=text, prediction_message=prediction_message)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)
