from emotion_data.emotions import EMOTIONS, DIMENSIONS
import random


OPPOSITE_FEELINGS_NAMES = {
    "optimism": "disapproval",
    "hope": "unbelief",
    "anxiety": "outrage",
    "love": "remorse",
    "guilt": "envy",
    "delight": "pessimism",
    "submission": "contempt",
    "curiosity": "cynicism",
    "sentimentality": "morbidness",
    "despair": "pride",
    "shame": "dominance",
    "bemusement": "dismay",
    "zeal": "horror",
    "acknowledgment": "listlessness",
    "devotion": "shame",
    "acquiescence": "impatience",
    "subservience": "hatred",
    "wariness": "disfavor",
    "petrification": "domination"
}


class Feeling(object):
    def __init__(self):
        self.name = ""
        self.emotions = []
        self.dimensions = []

    def __repr__(self):
        return "FeelingObject:" + self.name


def _get_feeling_emotions():
    bucket = {}
    feels = {'acknowledgement': ['serenity', 'acceptance'],
             'acquiescence': ['acceptance', 'apprehension'],
             'aggressiveness': ['anger', 'anticipation'],
             'anxiety': ['anticipation', 'fear'],
             'awe': ['fear', 'surprise'],
             'bemusement': ['interest', 'serenity'],
             'contempt': ['disgust', 'anger'],
             'curiosity': ['trust', 'surprise'],
             'cynicism': ['disgust', 'anticipation'],
             'delight': ['joy', 'surprise'],
             'despair': ['fear', 'sadness'],
             'devotion': ['ecstasy', 'admiration'],
             'disapproval': ['surprise', 'sadness'],
             'disfavor': ['annoyance', 'interest'],
             'dismay': ['distraction', 'pensiveness'],
             'dominance': ['anger', 'trust'],
             'domination': ['rage', 'vigilance'],
             'envy': ['sadness', 'anger'],
             'fatalism': ['vigilance', 'fear'],
             'guilt': ['joy', 'fear'],
             'hatred': ['loathing', 'rage'],
             'hope': ['anticipation', 'trust'],
             'horror': ['amazement', 'grief'],
             'impatience': ['boredom', 'annoyance'],
             'listlessness': ['pensiveness', 'boredom'],
             'love': ['joy', 'trust'],
             'morbidness': ['disgust', 'joy'],
             'optimism': ['anticipation', 'joy'],
             'outrage': ['surprise', 'anger'],
             'pessimism': ['sadness', 'anticipation'],
             'petrification': ['terror', 'amazement'],
             'pride': ['anger', 'joy'],
             'remorse': ['sadness', 'disgust'],
             'sentimentality': ['trust', 'sadness'],
             'shame': ['grief', 'loathing'],
             'submission': ['trust', 'fear'],
             'subservience': ['admiration', 'terror'],
             'unbelief': ['surprise', 'disgust'],
             'wariness': ['apprehension', 'distraction'],
             'zeal': ['vigilance', 'ecstasy']}
    for feeling in feels:
        emotions = feels[feeling]
        bucket[feeling] = []
        for e in emotions:
            bucket[feeling].append(EMOTIONS[e])
    return bucket


FEELINGS_TO_EMOTION_MAP = _get_feeling_emotions()


def _get_feelings():
    bucket = {}
    for feeling in FEELINGS_TO_EMOTION_MAP:
        f = Feeling()
        f.name = feeling.lower()
        for emotion in FEELINGS_TO_EMOTION_MAP[feeling]:
            f.emotions.append(emotion)
            d = DIMENSIONS.get(emotion.name)

            if isinstance(d, list):
                for dimension in d:
                    f.dimensions.append(dimension)
            elif d:
                f.dimensions.append(d)
        bucket[feeling.lower()] = f
    return bucket


FEELINGS = _get_feelings()


def get_feeling(name):
    return FEELINGS.get(name)


def random_feeling():
    return FEELINGS[random.choice(list(FEELINGS.keys()))]


if __name__ == "__main__":
    from pprint import pprint

    pprint(FEELINGS_TO_EMOTION_MAP)
    pprint(FEELINGS)