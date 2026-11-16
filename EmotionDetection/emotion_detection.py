"""Access the Watson NLP emotion prediction service."""

import requests

WATSON_URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
MODEL_ID = "emotion_aggregated-workflow_lang_en_stock"
EMOTIONS = ("anger", "disgust", "fear", "joy", "sadness")


def emotion_detector(text_to_analyze):
    """Return the five emotion scores and the strongest emotion."""
    empty_result = dict.fromkeys((*EMOTIONS, "dominant_emotion"))
    if not text_to_analyze.strip():
        return empty_result

    response = requests.post(
        WATSON_URL,
        headers={"grpc-metadata-mm-model-id": MODEL_ID},
        json={"raw_document": {"text": text_to_analyze}},
        timeout=15,
    )
    if response.status_code == 400:
        return empty_result

    response.raise_for_status()
    prediction = response.json()["emotionPredictions"][0]["emotion"]
    scores = {emotion: prediction[emotion] for emotion in EMOTIONS}
    return {**scores, "dominant_emotion": max(scores, key=scores.get)}
