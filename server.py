"""Serve the emotion detector as a Flask application."""

from flask import Flask, render_template, request

from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.get("/")
def index():
    """Render the emotion detection form."""
    return render_template("index.html")


@app.get("/emotionDetector")
def detect_emotion():
    """Analyze the query text and describe the result."""
    text = request.args.get("textToAnalyze", "")
    result = emotion_detector(text)
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"
    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
