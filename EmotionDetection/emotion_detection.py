import requests
import json

def emotion_detector(text_to_analyze):
    # Verify this URL matches exactly - NO trailing slash
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Ensure this is a POST request
    response = requests.post(url, json = myobj, headers = headers)
    
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        
        # Access the emotion data
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        
        emotion_dict = {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness']
        }
        dominant_emotion = max(emotion_dict, key=emotion_dict.get)
        
        emotion_dict['dominant_emotion'] = dominant_emotion
        return emotion_dict
    else:
        # Return the error details if it still fails
        return f"Error: {response.status_code}. Response: {response.text}"
