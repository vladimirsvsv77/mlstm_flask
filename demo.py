__author__ = 'VladimirSveshnikov'
from sentiment_classifier import SentimentClassifier
from codecs import open
import time
from flask import Flask, render_template, request, jsonify
import rake
app = Flask(__name__)


print ("Preparing classifier")
start_time = time.time()
classifier = SentimentClassifier()
print ("Classifier is ready")
print (time.time() - start_time, "seconds")
rake_object = rake.Rake("SmartStoplist.txt")


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


@app.route("/sentiment-api", methods=["GET"])
def api(text="", prediction_message=""):
    if request.method == "GET":
        text = request.args.get('text')
        prediction_message, class_pred, score = classifier.get_prediction_message(text)
        
    return jsonify({'class_pred': class_pred, 'score': str(score)}) 


@app.route("/keywords-api", methods=["GET"])
def keywords(text="", prediction_message=""):
    if request.method == "GET":
        text = request.args.get('text')
        keywords = rake_object.run(text)
        
    return jsonify({'keywords': keywords}) 


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=False)
