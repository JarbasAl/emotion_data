from emotion_data.deepmoji import get_emojis, get_emotions
from emotion_data.emotions import get_emotion, emotion_to_dimension, random_emotion, get_dimension
from emotion_data.feelings import get_feeling, random_feeling
from emotion_data.lexicons import get_emotion, get_sentiment, get_color, get_orientation, get_subjectivity


class EmotionAnalyzer(object):
    def __init__(self):
        pass

    @staticmethod
    def get_emotion(word):
        return get_emotion(word)

    @staticmethod
    def get_sentiment(word):
        return get_sentiment(word)

    @staticmethod
    def get_color(word):
        return get_color(word)

    @staticmethod
    def get_orientation(word):
        return get_orientation(word)

    @staticmethod
    def get_subjectivity(word):
        return get_subjectivity(word)

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
    def emotion(emotion_name):
        return get_emotion(emotion_name)

    @staticmethod
    def feeling(feeling_name):
        return get_feeling(feeling_name)

    @staticmethod
    def dimension(dimension_name):
        return get_dimension(dimension_name)

    @staticmethod
    def get(word):
        word = word.lower().strip()
        return get_emotion(word) or get_feeling(word) or get_dimension(word)

