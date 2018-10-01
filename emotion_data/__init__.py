from emotion_data.deepmoji import get_emojis, get_emotions
from emotion_data.emotions import get_emotion, emotion_to_dimension, random_emotion
from emotion_data.feelings import get_feeling, random_feeling


class EmotionAnalyzer(object):
    def __init__(self):
        pass

    @staticmethod
    def random_emotion():
        return random_emotion()

    @staticmethod
    def random_feeling():
        return random_feeling()

    @staticmethod
    def tag_emotions(sentence):
        return get_emotions(sentence)

    @staticmethod
    def tag_emojis(sentence):
        return get_emojis(sentence)

    @staticmethod
    def get_emotion(emotion):
        return get_emotion(emotion)

    @staticmethod
    def get_feeling(emotion):
        return get_feeling(emotion)