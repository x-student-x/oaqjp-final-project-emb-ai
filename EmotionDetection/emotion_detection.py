import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)


    dominant_emotion = None
    de_score = 0

    if response.status_code == 200:
        emotions_scores = formatted_response['emotionPredictions'][0]['emotion']
        for (a,b) in emotions_scores.items():
            if de_score < b:
                de_score = b
                dominant_emotion = a
        emotions_scores['dominant_emotion'] = dominant_emotion
        return emotions_scores
    elif response.status_code == 500:
        return dominant_emotion
