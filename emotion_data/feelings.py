from emotion_data import get_emotion, get_dyad
import random


class Feeling(object):
    def __init__(self):
        self.name = ""
        self.emotions = []
        self.dyads = []

    def __repr__(self):
        return "FeelingObject:" + self.name


def _get_feelings():
    feels = {
        "Optimism": ["Anticipation", "joy"],
        "Disapproval": ["Surprise", "Sadness"],
        "Hope": ["Anticipation", "Trust"],
        "Unbelief": ["Surprise", "Disgust"],
        "Anxiety": ["Anticipation", "Fear"],
        "Outrage": ["Surprise", "Anger"],
        "Love": ["Joy", "Trust"],
        "Remorse": ["Sadness", "Disgust"],
        "Guilt": ["Joy", "Fear"],
        "Envy": ["Sadness", "Anger"],
        "Delight": ["Joy", "Surprise"],
        "Pessimism": ["Sadness", "Anticipation"],
        "Submission": ["Trust", "Fear"],
        "Contempt": ["Disgust", "Anger"],
        "Curiosity": ["Trust", "Surprise"],
        "Cynicism": ["Disgust", "Anticipation"],
        "Sentimentality": ["Trust", "Sadness"],
        "Morbidness": ["Disgust", "Joy"],
        "Awe": ["Fear", "Surprise"],
        "Aggressiveness": ["Anger", "Anticipation"],
        "Despair": ["Fear", "Sadness"],
        "Pride": ["Anger", "Joy"],
        "shame": ["Fear", "Disgust"],
        "Dominance": ["Anger", "Trust"],
        "Bemusement": ["Interest", "Serenity"],
        "Dismay": ["Distraction", "Pensiveness"],
        "Zeal": ["Vigilance", "Ecstasy"],
        "Horror": ["Amazement", "Grief"],
        "Acknowledgement": ["Serenity", "Acceptance"],
        "Listlessness": ["Pensiveness", "Boredom"],
        "Devotion": ["Ecstasy", "Admiration"],
        "Shame": ["Grief", "Loathing"],
        "Acquiescence": ["acceptance", "Apprehension"],
        "Impatience": ["Boredom", "Annoyance"],
        "Subservience": ["Admiration", "Terror"],
        "Hatred": ["Loathing", "Rage"],
        "Wariness": ["Apprehension", "Distraction"],
        "Disfavor": ["Annoyance", "Interest"],
        "Petrification": ["Terror", "Amazement"],
        "Domination": ["Rage", "Vigilance"]
    }
    map = {}
    for feeling in feels:
        f = Feeling()
        f.name = feeling.lower()
        for emotion in feels[feeling]:
            f.emotions.append(get_emotion(emotion.lower()))
            d = get_dyad(emotion.lower())

            if isinstance(d, list):
                for dyad in d:
                    f.dyads.append(dyad)
            elif d:
                f.dyads.append(d)
        map[feeling.lower()] = f
    return map


FEELINGS_MAP = _get_feelings()


def get_feeling(name):
    return FEELINGS_MAP.get(name)


def random_feeling():
    return FEELINGS_MAP[random.choice(list(FEELINGS_MAP.keys()))]

