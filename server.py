"""Server for emotion detection"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """perform emotion detection"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)


    de_score = 0

    if response is None:
        return "Invalid input ! Try again"

    for b in response.values():
        if isinstance(b, float):
            if de_score < float(b):
                de_score = float(b)



        final_response = "For the given statement, the system response is "

        final_response += f"\'anger\' : {response['anger']}, \'disgust\' : {response['disgust']}," \
        f" \'fear\' : {response['fear']}, \'joy\' : {response['joy']}," \
        f" \'Sadness\' : {response['sadness']}."

        final_response += f"\n The dominant emotion is {response['dominant_emotion']}"

        return final_response

@app.route("/")
def render_index_page():
    """render page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
