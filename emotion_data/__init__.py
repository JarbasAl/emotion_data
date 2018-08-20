import random


class EmotionDyad(object):
    def __init__(self):
        self.dimension = "0"
        self.mild_emotion = ""
        self.mild_opposite = ""
        self.basic_emotion = ""
        self.basic_opposite = ""
        self.intense_emotion = ""
        self.intense_opposite = ""

    @property
    def name(self):
        return self.dimension

    def __repr__(self):
        return "DyadObject:" + self.dimension


class Emotion(object):
    def __init__(self):
        self.name = ""
        self.intensity = "mild"  # mild, basic, intense
        self.is_primary = True
        self.is_secondary = False
        self.is_tertiary = False
        self.valence = 0  # -1 negative, 0 neutral, 1, positive
        self.kind = ""  # Related to object properties, Future appraisal, Event-related, Self-appraisal, Social, Cathected
        self.dimension = ""  # Sensitivity, Attention, Pleansantness, Aptitude
        self.emotional_flow = 0  # +3 to -3
        self.dyad = None  # EmotionDyad object
        self.opposite = ""  # opposite emotion name
        self.type = "neutral"
        self.parent_emotion = None

    @property
    def is_composite(self):
        return False

    def __repr__(self):
        return "EmotionObject:" + self.name


class CompositeEmotion(Emotion):
    def __init__(self):
        Emotion.__init__(self)
        self.name = ""
        self.intensity = "intense"  # mild, basic, intense
        self.is_primary = True
        self.is_secondary = False
        self.is_tertiary = False
        self.kind = "composite"  # Related to object properties, Future appraisal, Event-related, Self-appraisal, Social, Cathected
        self.valence = 0  # -1 negative, 0 neutral, 1, positive
        self.components = []

    @property
    def is_composite(self):
        return True

    def __repr__(self):
        return "CompositeEmotionObject:" + self.name


def _get_dyads():
    dyads = {
        "sensitivity": ["Serenity", "Pensiveness", "Joy", "Sadness", "Ecstasy", "Grief"],
        "attention": ["Acceptance", "Boredom", "Trust", "Disgust", "Admiration", "Loathing"],
        "pleasentness": ["Apprehension", "Annoyance", "Fear", "Anger", "Terror", "Rage"],
        "aptitude": ["Distraction", "Interest", "Surprise", "Anticipation", "Amazement", "Vigilance"],
    }
    dyad_map = {}
    for d in dyads:
        dyad = EmotionDyad()
        dyad.dimension = d
        dyad.mild_emotion = dyads[d][0].lower()
        dyad.mild_opposite = dyads[d][1].lower()
        dyad.basic_emotion = dyads[d][2].lower()
        dyad.basic_opposite = dyads[d][3].lower()
        dyad.intense_emotion = dyads[d][4].lower()
        dyad.intense_opposite = dyads[d][5].lower()
        dyad_map[d] = dyad
    return dyad_map


DYADS = _get_dyads()


def _get_dyads_map():
    dyads = {
        "sensitivity": ["Serenity", "Pensiveness", "Joy", "Sadness", "Ecstasy", "Grief"],
        "attention": ["Acceptance", "Boredom", "Trust", "Disgust", "Admiration", "Loathing"],
        "pleasentness": ["Apprehension", "Annoyance", "Fear", "Anger", "Terror", "Rage"],
        "aptitude": ["Distraction", "Interest", "Surprise", "Anticipation", "Amazement", "Vigilance"],
    }
    dyad_map = {}
    for d in dyads:
        for i in range(6):
            dyad_map[dyads[d][i].lower()] = DYADS[d]
    return dyad_map


DYAD_MAP = _get_dyads_map()


def _get_opposite_emotion_map():
    map = {"love": "hate"}
    for d in DYADS:
        dyad = DYADS[d]
        map[dyad.mild_emotion] = dyad.mild_opposite
        map[dyad.mild_opposite] = dyad.mild_emotion
        map[dyad.basic_emotion] = dyad.basic_opposite
        map[dyad.basic_opposite] = dyad.basic_emotion
        map[dyad.intense_emotion] = dyad.intense_opposite
        map[dyad.intense_opposite] = dyad.intense_emotion
    return map


POSITIVE_EMOTIONS = ["interest", "curiosity", "enthusiasm", "amusement",
                     "attraction", "desire", "admiration", "surprise", "love",
                     "hope", "excitement", "gratitude", "thankfulness",
                     "joy", "elation", "triumph", "jubilation", "patience",
                     "contentment", "humility", "modesty", "charity", "sympathy"]
NEGATIVE_EMOTIONS = ["indifference", "habituation", "boredom", "aversion",
                     "disgust", "revulsion", "alarm", "panic", "fear", "anxiety",
                     "dread", "anger", "rage", "sorrow", "grief", "frustration",
                     "disappointment", "pride", "arrogance", "avarice", "greed",
                     "miserliness", "envy", "jealousy", "cruelty", "hate"]

OPPOSITE_EMOTION_MAP = _get_opposite_emotion_map()

DIMENSION_MAP = {"sensitivity": ["rage", "anger", "annoyance", "apprehension", "fear", "terror"],
                 "attention": ["vigilance", "anticipation", "interest", "distraction", "surprise", "amazement"],
                 "pleasantness": ["ecstasy", "joy", "serenity", "pensiveness", "sadness", "grief"],
                 "aptitude": ["admiration", "trust", "acceptance", "boredom", "disgust", "loathing"]}

EMOTION_KIND_MAP = {"related to object properties":
                        ["interest", "curiosity", "enthusiasm", "indifference", "habituation", "boredom",
                         "attraction", "desire", "admiration", "aversion", "disgust", "revulsion",
                         "surprise", "amusement", "alarm", "panic"],
                    'future appraisal': ["hope", "excitement", "fear", "anxiety", "dread"],
                    'event related': ["gratitude", "thankfulness", "anger", "rage", "joy", "elation", "triumph",
                                      "jubilation", "sorrow", "grief", "patience", "frustration", "disappointment",
                                      "contentment", "discontentment", "restlessness"],
                    'self appraisal': ["humility", "modesty", "pride", "arrogance"],
                    'social': ["charity", "sympathy", "avarice", "greed", "miserliness", "envy", "jealousy", "cruelty"],
                    'cathected': ["love", "hate"],
                    }

HUMAINE_MAP = {
    "negative and forceful":
        ["anger", "annoyance", "contempt", "disgust", "irritation"],
    "negative and passive":
        ["boredom", "despair", "disappointment", "hurt", "sadness"],
    "caring":
        ["affection", "empathy", "friendliness", "love"],
    "negative and not in control":
        ["Anxiety", "Embarrassment", "fear", "Helplessness", "Powerlessness", "Worry"],
    "agitation":
        ["Stress", "Shock", "Tension"],
    "positive thoughts":
        ["Courage", "Hope", "Humility", "Satisfaction", "Trust"],
    "negative thoughts":
        ["Pride", "Doubt", "Envy", "Frustration", "Guilt", "Shame"],
    "positive and lively":
        ["Amusement", "Delight", "Elation", "Excitement", "Happiness", "Joy", "Pleasure"],
    "quiet positive":
        ["Calmness", "Contentment", "Relaxation", "Relief", "Serenity"],
    "reactive":
        ["Interest", "Politeness", "Surprise"]
}

EMOTION_TREE = {
    'anger': [{'disgust': ['revulsion',
                           'contempt',
                           'loathing'],
               'envy': ['jealousy'],
               'exasperation': ['frustration'],
               'irritability': ['aggravation',
                                'agitation',
                                'annoyance',
                                'grouchy',
                                'grumpy',
                                'crosspatch'],
               'rage': ['outrage',
                        'fury',
                        'wrath',
                        'hostility',
                        'ferocity',
                        'bitterness',
                        'hate',
                        'scorn',
                        'spite',
                        'vengefulness',
                        'dislike',
                        'resentment'],
               'torment': []}],
    'fear': [{'horror': ['alarm',
                         'shock',
                         'fright',
                         'terror',
                         'panic',
                         'hysteria',
                         'mortification'],
              'nervousness': ['anxiety',
                              'suspense',
                              'uneasiness',
                              'apprehension',
                              'worry',
                              'distress',
                              'dread']}],
    'joy': [{'cheerfulness': ['amusement',
                              'bliss',
                              'gaiety',
                              'glee',
                              'jolliness',
                              'joviality',
                              'delight',
                              'enjoyment',
                              'gladness',
                              'happiness',
                              'jubilation',
                              'elation',
                              'satisfaction',
                              'ecstasy',
                              'euphoria'],
             'contentment': ['pleasure'],
             'enthrallment': ['rapture'],
             'optimism': ['eagerness',
                          'hope'],
             'pride': ['triumph'],
             'relief': [],
             'zest': ['enthusiasm',
                      'zeal',
                      'excitement',
                      'thrill',
                      'exhilaration']}],
    'love': [{'affection': ['adoration',
                            'fondness',
                            'liking',
                            'attraction',
                            'caring',
                            'tenderness',
                            'compassion',
                            'sentimentality'],
              'longing': [],
              'lust': ['desire',
                       'passion',
                       'infatuation']}],
    'sadness': [{'disappointment': ['dismay',
                                    'displeasure'],
                 'misery': ['depression',
                            'despair',
                            'gloom',
                            'glumness',
                            'unhappiness',
                            'grief',
                            'sorrow',
                            'woe',
                            'melancholy'],
                 'neglect': ['alienation',
                             'defeatism',
                             'dejection',
                             'embarrassment',
                             'homesickness',
                             'humiliation',
                             'insecurity',
                             'insult',
                             'isolation',
                             'loneliness',
                             'rejection'],
                 'shame': ['guilt',
                           'regret',
                           'remorse'],
                 'suffering': ['agony',
                               'anguish',
                               'hurt'],
                 'sympathy': ['pity',
                              'mono no aware']}],
    'surprise': [{'amazement': [],
                  'astonishment': []}]
}

COMPOSITE_EMOTIONS = {
    "aggressiveness": [("rage", "vigilance")],
    "rejection": [("rage", "amazement")],
    "rivalry": [("rage", "admiration")],
    "contempt": [("rage", "loathing")],

    "anxiety": [("terror", "vigilance")],
    "awe": [("terror", "amazement")],
    "submission": [("terror", "admiration")],
    "coercion": [("terror", "loathing")],

    "optimism": [("ecstasy", "vigilance")],
    "frivolity": [("ecstasy", "amazement")],
    "love": [("ecstasy", "admiration")],
    "gloat": [("ecstasy", "loathing")],

    "frustration": [("grief", "vigilance")],
    "disapproval": [("grief", "amazement")],
    "envy": [("grief", "admiration")],
    "remorse": [("grief", "loathing")]
}


def _get_emotion_map():
    map = {}

    # get the basic emotions from each dimension
    flows = [3, 2, 1, -1, -2, -3]
    for dimension in DIMENSION_MAP:
        for i, name in enumerate(DIMENSION_MAP[dimension]):
            emotion = Emotion()
            emotion.name = name
            emotion.dimension = dimension
            emotion.emotional_flow = flows[i]
            if abs(emotion.emotional_flow) == 1:
                emotion.intensity == "basic"
            elif abs(emotion.emotional_flow) == 3:
                emotion.intensity == "intense"
            # add the corresponding dyad
            if name in DYAD_MAP:
                emotion.dyad = DYAD_MAP[name]

            # tag the opposite emotion
            if name in OPPOSITE_EMOTION_MAP:
                emotion.opposite = OPPOSITE_EMOTION_MAP[name]

            # add a kind if applicable
            for kind in EMOTION_KIND_MAP:
                if name in EMOTION_KIND_MAP[kind]:
                    emotion.kind = kind
                    break

            # add a type if applicable
            for emo_type in HUMAINE_MAP:
                if name in HUMAINE_MAP[emo_type]:
                    emotion.type = emo_type
                    break
            map[name] = emotion

    # create composite emotions for dimension combinations
    for emotion in COMPOSITE_EMOTIONS:
        for t in COMPOSITE_EMOTIONS[emotion]:
            e = CompositeEmotion()
            e.name = emotion
            for s in t:
                e.components.append(map.get(s))
            for kind in EMOTION_KIND_MAP:
                if emotion in EMOTION_KIND_MAP[kind]:
                    e.kind = kind
                    break
            for emo_type in HUMAINE_MAP:
                if emotion in HUMAINE_MAP[emo_type]:
                    e.type = emo_type
                    break
            map[emotion] = e

    # navigate tree
    for primary in EMOTION_TREE:
        # primary emotions
        emotion = map.get(primary)
        if not emotion:
            emotion = Emotion()
            emotion.name = primary
        emotion.is_primary = True
        emotion.is_secondary = False
        emotion.is_tertiary = False
        map[primary] = emotion
        # secondary emotions
        for secondary in EMOTION_TREE[primary]:
            for name in secondary:
                secondary_emotion = map.get(name)
                if not secondary_emotion:
                    secondary_emotion = Emotion()
                    secondary_emotion.name = name
                secondary_emotion.is_primary = False
                secondary_emotion.is_secondary = True
                secondary_emotion.is_tertiary = False
                secondary_emotion.parent_emotion = emotion
                if secondary_emotion.dyad is None:
                    # use parents dyad
                    secondary_emotion.dyad = emotion.dyad
                if not secondary_emotion.dimension:
                    # use parents dimension
                    secondary_emotion.dimension = emotion.dimension
                if not secondary_emotion.emotional_flow:
                    # use parents flow
                    secondary_emotion.emotional_flow = emotion.emotional_flow
                if not secondary_emotion.opposite:
                    # use parents opposite
                    secondary_emotion.opposite = emotion.opposite
                if not secondary_emotion.valence:
                    # use parents valence
                    secondary_emotion.valence = emotion.valence * 0.9
                if secondary_emotion.type == "neutral":
                    # use parents type
                    secondary_emotion.type = emotion.type
                if not secondary_emotion.kind:
                    # use parents kind
                    secondary_emotion.kind = emotion.kind

                map[name] = emotion

                # tertiary emotions
                for tertiary in secondary[name]:
                    tertiary_emotion = map.get(tertiary)
                    if not tertiary_emotion:
                        tertiary_emotion = Emotion()
                        tertiary_emotion.name = tertiary
                    tertiary_emotion.is_primary = False
                    tertiary_emotion.is_secondary = False
                    tertiary_emotion.is_tertiary = True
                    tertiary_emotion.parent_emotion = secondary_emotion
                    if tertiary_emotion.dyad is None:
                        # use parents dyad
                        tertiary_emotion.dyad = secondary_emotion.dyad
                    if not tertiary_emotion.dimension:
                        # use parents dimension
                        tertiary_emotion.dimension = secondary_emotion.dimension
                    if not tertiary_emotion.emotional_flow:
                        # use parents flow
                        tertiary_emotion.emotional_flow = secondary_emotion.emotional_flow
                    if not tertiary_emotion.opposite:
                        # use parents opposite
                        tertiary_emotion.opposite = secondary_emotion.opposite
                    if not tertiary_emotion.valence:
                        # use parents valence
                        tertiary_emotion.valence = secondary_emotion.valence * 0.9
                    if tertiary_emotion.type == "neutral":
                        # use parents type
                        tertiary_emotion.type = secondary_emotion.type
                    if not tertiary_emotion.kind:
                        # use parents kind
                        tertiary_emotion.kind = secondary_emotion.kind

                    map[tertiary] = tertiary_emotion

    # assign valence
    for name in map:
        parent = map[name].parent_emotion
        if name in POSITIVE_EMOTIONS:
            map[name].valence = 1
        elif name in NEGATIVE_EMOTIONS:
            map[name].valence = -1
        elif parent and parent.name in POSITIVE_EMOTIONS:
            map[name].valence = 1
        elif parent and parent.name in NEGATIVE_EMOTIONS:
            map[name].valence = -1
        elif "negative" in map[name].type:
            map[name].valence = -1
        elif "positive" in map[name].type:
            map[name].valence = 1
        elif map[name].emotional_flow:
            map[name].valence = 1
        else:
            map[name].valence = 0

    # assign kind
    for name in map:
        if not map[name].kind and map[name].dyad:
            map[name].kind = map[map[name].dyad.basic_emotion].kind
    return map


EMOTION_MAP = _get_emotion_map()

EMOTION_NAMES = [EMOTION_MAP[e].name for e in EMOTION_MAP]

POSITIVE_EMOTIONS = [EMOTION_MAP[e].name for e in EMOTION_MAP if EMOTION_MAP[e].valence]

NEGATIVE_EMOTIONS = [EMOTION_MAP[e].name for e in EMOTION_MAP if EMOTION_MAP[e].valence < 0]

NEUTRAL_EMOTIONS = [EMOTION_MAP[e].name for e in EMOTION_MAP if EMOTION_MAP[e].valence == 0]

DIMENSION_MAP = {"sensitivity": [EMOTION_MAP[e].name for e in EMOTION_MAP if EMOTION_MAP[e].dimension == "sensitivity"],
                 "attention": [EMOTION_MAP[e].name for e in EMOTION_MAP if EMOTION_MAP[e].dimension == "attention"],
                 "pleasantness": [EMOTION_MAP[e].name for e in EMOTION_MAP if EMOTION_MAP[e].dimension == "pleasantness"],
                 "aptitude": [EMOTION_MAP[e].name for e in EMOTION_MAP if EMOTION_MAP[e].dimension == "aptitude"]}

EMOTION_KIND_MAP = {"related to object properties":
                        [EMOTION_MAP[e].name for e in EMOTION_MAP if EMOTION_MAP[e].kind == "related to object properties"],
                    'future appraisal': [EMOTION_MAP[e].name for e in EMOTION_MAP if EMOTION_MAP[e].kind == "future appraisal"],
                    'event related': [EMOTION_MAP[e].name for e in EMOTION_MAP if EMOTION_MAP[e].kind == "event related"],
                    'self appraisal': [EMOTION_MAP[e].name for e in EMOTION_MAP if EMOTION_MAP[e].kind == "self appraisal"],
                    'social': [EMOTION_MAP[e].name for e in EMOTION_MAP if EMOTION_MAP[e].kind == "social"],
                    'cathected': [EMOTION_MAP[e].name for e in EMOTION_MAP if EMOTION_MAP[e].kind == "cathected"]
                    }

# TODO update from generated emotions map
# DYADS_MAP = {}


def random_emotion():
    return EMOTION_MAP[random.choice(list(EMOTION_MAP.keys()))]


def get_emotion(name):
    return EMOTION_MAP.get(name)


def get_dyad(name):
    emotion = get_emotion(name)
    if emotion:
        if emotion.is_composite:
            return [e.dyad for e in emotion.components if e.dyad]
        return emotion.dyad
    return None


