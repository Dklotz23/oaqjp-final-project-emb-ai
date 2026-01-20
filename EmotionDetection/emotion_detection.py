
import requests
import json


def emotion_detector(text_to_analyze):
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=data, headers=headers)

    data = json.loads(response.text)

    json_data = data['emotionPredictions'][0]['emotion']

    dominant_emotion = max(json_data, key=json_data.get)

    return {
        'anger': json_data['anger'],
        'disgust': json_data['disgust'], 
        'fear': json_data['fear'],
        'joy': json_data['joy'],
        'sadness': json_data['sadness'],
        'dominant_emotion': dominant_emotion
           }