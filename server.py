
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def run_emotion_detector():
    text_to_analyize = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyize)

    formated_text = f"""For the given statement, the system response is anger: {response['anger']}, 
    disgust: {response['disgust']}, fear: {response['fear']}, 
    joy: {response['joy']} and sadness: {response['sadness']}. 
    The dominant emotion is {response['dominant_emotion']}."""

    return formated_text

@app.route("/")
def render_index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="", port=5000)

