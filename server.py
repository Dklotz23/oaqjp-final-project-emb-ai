"""
Server python file
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def run_emotion_detector():
    """
    Gets text from input on site and runs it through the emotion detector.
    Returns formated text string. 
    """
    text_to_analyize = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyize)

    if response is None:
        formated_text = 'Invalid Text! Please try again!'
    else:
        formated_text = f"""For the given statement,
        the system response is anger: {response['anger']},
        disgust: {response['disgust']}, fear: {response['fear']}, 
        joy: {response['joy']} and sadness: {response['sadness']}. 
        The dominant emotion is {response['dominant_emotion']}.
        """

    return formated_text


@app.route("/")
def render_index():
    """
    Display the main page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="", port=5000)
