from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    dominant_emotion = ''
    de_score = 0
    for (a,b) in response.items():
        if isinstance(b, float):
            if de_score < float(b):
                de_score = float(b)
                dominant_emotion = a


    final_response = "For the given statement, the system response is {} : {}, {} : {}, {} : {}, {} : {}, {} : {}.".format("\'anger\'", response['anger'],
                                                                                      "\'disgust\'", response['disgust'],
                                                                                      "\'fear\'", response['fear'],
                                                                                      "\'joy\'", response['joy'],
                                                                                      "\'sadness\'", response['sadness'],
                                                                                      )
    final_response += f"\n The dominant emotion is {dominant_emotion}"

    return final_response



@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
