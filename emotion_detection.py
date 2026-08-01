"""
Este modulo analiza las emociones de un texto con la libretia bert de I
M Wahtson, usada en la url.
"""
import json
import request


def emotion_detector(text_to_analyse):
    """
    funcion que devuelve la respuesta sentimiento y puntaje.
    """
    if not text_to_analyse or not text_to_analyse.strip():
        return {"label": None, "score": None}

    url = ('https://sn-watson-sentiment-bert.labs.skills.network/'
           'v1/watson.runtime.nlp.v1/NlpService/SentimentPredict')
    headers = {
        "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
    }
    myobj = {"raw_document": {"text": text_to_analyse}}

    try:
        response = requests.post(url, json=myobj, headers=headers, timeout=10)

        if response.status_code == 200:
            formatted_response = json.loads(response.text)
            label = formatted_response["documentSentiment"]["label"]
            score = formatted_response["documentSentiment"]["score"]
        else:
            label = None
            score = None
    except Exception as e:
        print(f"Error llamando a la API: {e}")
        label = None
        score = None

    return {"label": label, "score": score}

