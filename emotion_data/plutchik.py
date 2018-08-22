from emotion_data.reference_maps import EMOTION_CONTRASTS, POSITIVE, NEGATIVE


PRIMARY_EMOTION_NAMES = ["serenity", "pensiveness", "acceptance", "boredom", "apprehension", "annoyance", "distraction",
                    "interest"]
SECONDARY_EMOTIONS_NAMES = ["joy", "sadness", "trust", "disgust", "fear", "anger", "surprise", "anticipation"]

TERTIARY_EMOTIONS_NAMES = ["ecstasy", "grief", "admiration", "loathing", "terror", "rage", "amazement", "vigilance"]

HOURGLASS_OF_EMOTIONS = {"sensitivity": ["rage", "anger", "annoyance", "apprehension", "fear", "terror"],
                         "attention": ["vigilance", "anticipation", "interest", "distraction", "surprise", "amazement"],
                         "pleasantness": ["ecstasy", "joy", "serenity", "pensiveness", "sadness", "grief"],
                         "aptitude": ["admiration", "trust", "acceptance", "boredom", "disgust", "loathing"]}

COMPOSITE_EMOTIONS_NAMES = {
    "aggressiveness": ["rage", "vigilance"],
    "rejection": ["rage", "amazement"],
    "rivalry": ["rage", "admiration"],
    "contempt": ["rage", "loathing"],

    "anxiety": ["terror", "vigilance"],
    "awe": ["terror", "amazement"],
    "submission": ["terror", "admiration"],
    "coercion": ["terror", "loathing"],

    "optimism": ["ecstasy", "vigilance"],
    "frivolity": ["ecstasy", "amazement"],
    "love": ["ecstasy", "admiration"],
    "gloat": ["ecstasy", "loathing"],

    "frustration": ["grief", "vigilance"],
    "disapproval": ["grief", "amazement"],
    "envy": ["grief", "admiration"],
    "remorse": ["grief", "loathing"]
}

OPPOSITE_EMOTIONS_NAMES = {
    "annoyance": "apprehension",
    "interest": "distraction",
    "serenity": "pensiveness",
    "acceptance": "boredom",
    "trust": "disgust",
    "joy": "sadness",
    "anticipation": "surprise",
    "anger": "fear",
    "rage": "terror",
    "vigilance": "amazement",
    "ecstasy": "grief",
    "admiration": "loathing",
    "apprehension": "annoyance",
    "distraction": "interest",
    "pensiveness": "serenity",
    "boredom": "acceptance",
    "disgust": "trust",
    "sadness": "joy",
    "surprise": "anticipation",
    "fear": "anger",
    "terror": "rage",
    "amazement": "vigilance",
    "grief": "ecstasy",
    "loathing": "admiration",
    # composite
    "contempt": "submission",
    "rivalry": "coercion",
    "anxiety": "rejection",
    "awe": "aggressiveness",
    "love": "remorse",
    "envy": "gloat",
    "frivolity": "frustration",
    "disapproval": "optimism",
    "submission": "contempt",
    "coercion": "rivalry",
    "rejection": "anxiety",
    "aggressiveness": "awe",
    "remorse": "love",
    "gloat": "envy",
    "frustration": "frivolity",
    "optimism": "disapproval"
}


# TODO science this instead of eye balling
# expand emotion contrasts, these are manually tagged and a matter of opinion

EMOTION_KIND_NAMES = EMOTION_CONTRASTS.copy()
EMOTION_KIND_NAMES['cathected'].append("contempt")

EMOTION_KIND_NAMES['related to object properties'].append("amazement")
EMOTION_KIND_NAMES['related to object properties'].append("awe")
EMOTION_KIND_NAMES['related to object properties'].append("annoyance")

EMOTION_KIND_NAMES['event related'].append("remorse")
EMOTION_KIND_NAMES['event related'].append("terror")
EMOTION_KIND_NAMES['event related'].append("disapproval")
EMOTION_KIND_NAMES['event related'].append("aggressiveness")
EMOTION_KIND_NAMES['event related'].append("sadness")
EMOTION_KIND_NAMES['event related'].append("acceptance")
EMOTION_KIND_NAMES['event related'].append("ecstasy")
EMOTION_KIND_NAMES['event related'].append("apprehension")
EMOTION_KIND_NAMES['event related'].append("loathing")
EMOTION_KIND_NAMES['event related'].append("gloat") # TODO where does this fit better?

EMOTION_KIND_NAMES['social'].append("coercion")
EMOTION_KIND_NAMES['social'].append("trust")
EMOTION_KIND_NAMES['social'].append("submission")
EMOTION_KIND_NAMES['social'].append("rivalry")
EMOTION_KIND_NAMES['social'].append("rejection")
EMOTION_KIND_NAMES['social'].append("frivolity") # TODO where does this fit better?

EMOTION_KIND_NAMES['future appraisal'].append("pensiveness")
EMOTION_KIND_NAMES['future appraisal'].append("optimism")
EMOTION_KIND_NAMES['future appraisal'].append("vigilance")
EMOTION_KIND_NAMES['future appraisal'].append("distraction")
EMOTION_KIND_NAMES['future appraisal'].append("serenity")
EMOTION_KIND_NAMES['future appraisal'].append("anticipation")


class Emotion(object):
    def __init__(self, name, dimension=None):
        self.name = name
        self.dimension = dimension  # EmotionDimension object

    @property
    def triggered_reactions(self):
        from emotion_data.behaviour import REACTION_TO_EMOTION_MAP, REACTIONS
        reactions = []
        for reaction in REACTION_TO_EMOTION_MAP:
            emo = REACTION_TO_EMOTION_MAP[reaction]
            if emo.name == self.name:
                reactions.append(REACTIONS[reaction])
        return reactions

    @property
    def base_emotion(self):
        if self.is_primary:
            return self
        if self.emotional_flow < 0:
            return self.dimension.basic_opposite
        else:
            return self.dimension.basic_emotion

    @property
    def parent_emotion(self):
        if self.is_primary or self.is_composite:
            return None
        if self.is_secondary:
            if self.emotional_flow < 0:
                return self.dimension.basic_opposite
            elif self.emotional_flow > 0:
                return self.dimension.basic_emotion
        elif self.is_tertiary:
            if self.emotional_flow < 0:
                return self.dimension.mild_opposite
            elif self.emotional_flow > 0:
                return self.dimension.mild_emotion
        return None

    @property
    def opposite_emotion(self):
        if self.is_primary and self.emotional_flow > 0:
            return self.dimension.basic_opposite
        elif self.is_primary and self.emotional_flow < 0:
            return self.dimension.basic_emotion
        elif self.is_secondary and self.emotional_flow > 0:
            return self.dimension.mild_opposite
        elif self.is_secondary and self.emotional_flow < 0:
            return self.dimension.mild_emotion
        elif self.is_tertiary and self.emotional_flow > 0:
            return self.dimension.intense_opposite
        elif self.is_tertiary and self.emotional_flow < 0:
            return self.dimension.intense_emotion
        return None

    @property
    def is_primary(self):
        return self.name in PRIMARY_EMOTION_NAMES and not self.is_composite

    @property
    def is_secondary(self):
        return self.name in SECONDARY_EMOTIONS_NAMES and not self.is_composite

    @property
    def is_tertiary(self):
        return self.name in TERTIARY_EMOTIONS_NAMES and not self.is_composite

    @property
    def type(self):
        # TODO science this instead of eye balling
        if self.is_composite:
            pass
        if self.emotional_flow < 0:
            # negative
            if self.dimension.axis == "sensitivity":
                return "negative and forceful"
            if self.dimension.axis == "aptitude":
                return "negative and passive"
            if self.dimension.axis == "attention":
                return "reactive"
            if self.dimension.axis == "pleasantness":
                return "negative and not in control"
        else:
            # positive
            if self.dimension.axis == "attention":
                return "agitation"
            if self.dimension.axis == "pleasantness":
                return "positive and lively"
            if self.dimension.axis == "aptitude":
                return "quiet positive"
            if self.dimension.axis == "sensitivity":
                return "negative and forceful"

    @property
    def kind(self):
        # TODO science this instead of eye balling
        for kind in EMOTION_KIND_NAMES:
            if self.name in EMOTION_KIND_NAMES[kind]:
                return kind
        # if self.parent_emotion:
        #    return self.parent_emotion.kind
        # if self.base_emotion and not self.is_primary:
        #    return self.base_emotion.kind
        # if self.opposite_emotion and self.opposite_emotion.kind:
        #    return self.opposite_emotion.kind
        return ""

    @property
    def emotional_flow(self):
        if self.is_primary and self.dimension.basic_emotion.name == self.name:
            return 1
        elif self.is_primary and self.dimension.basic_opposite.name == self.name:
            return -1
        elif self.is_secondary and self.dimension.mild_emotion.name == self.name:
            return 2
        elif self.is_secondary and self.dimension.mild_opposite.name == self.name:
            return -2
        elif self.is_tertiary and self.dimension.intense_emotion.name == self.name:
            return 3
        elif self.is_tertiary and self.dimension.intense_opposite.name == self.name:
            return -3

        return 0

    @property
    def valence(self):
        if self.emotional_flow:
            return 1
        elif self.emotional_flow < 0:
            return - 1
        elif self.name in POSITIVE:
            return 1
        elif self.name in NEGATIVE:
            return -1
        elif "negative" in self.type:
            return -1
        elif "positive" in self.type:
            return 1
        return 0

    @property
    def intensity(self):
        if abs(self.emotional_flow) == 1:
            return "basic"
        if abs(self.emotional_flow) == 2:
            return "mild"
        if abs(self.emotional_flow) == 3:
            return "intense"
        if self.parent_emotion:
            return self.parent_emotion.intensity
        return ""

    @property
    def is_composite(self):
        return False

    def __repr__(self):
        return "EmotionObject:" + self.name


class EmotionalDimension(object):
    def __init__(self):
        self.axis = ""  # sensitivity, attention, pleasantness, aptitude
        self.mild_emotion = None
        self.mild_opposite = None
        self.basic_emotion = None
        self.basic_opposite = None
        self.intense_emotion = None
        self.intense_opposite = None

    @property
    def name(self):
        return str(self.axis)

    def __repr__(self):
        return "DimensionObject:" + self.name


def _get_dimensions():
    # map dimension name to object
    dimension_map = {}
    for d in HOURGLASS_OF_EMOTIONS:
        dimension = EmotionalDimension()
        dimension.axis = d

        # create the emotion objects
        dimension.intense_emotion = Emotion(HOURGLASS_OF_EMOTIONS[d][0].lower())
        dimension.mild_emotion = Emotion(HOURGLASS_OF_EMOTIONS[d][1].lower())
        dimension.basic_emotion = Emotion(HOURGLASS_OF_EMOTIONS[d][2].lower())
        dimension.basic_opposite = Emotion(HOURGLASS_OF_EMOTIONS[d][3].lower())
        dimension.mild_opposite = Emotion(HOURGLASS_OF_EMOTIONS[d][4].lower())
        dimension.intense_opposite = Emotion(HOURGLASS_OF_EMOTIONS[d][5].lower())

        # pass the dimention reference to the emotion
        dimension.basic_emotion.dimension = dimension
        dimension.basic_opposite.dimension = dimension
        dimension.mild_emotion.dimension = dimension
        dimension.mild_opposite.dimension = dimension
        dimension.intense_emotion.dimension = dimension
        dimension.intense_opposite.dimension = dimension

        dimension_map[d] = dimension
    return dimension_map


DIMENSIONS = _get_dimensions()


class CompositeEmotion(Emotion):
    def __init__(self, name):
        Emotion.__init__(self, name)
        self.name = name
        self.components = []

    @property
    def type(self):
        # TODO science this instead of eye balling
        if self.emotional_flow < 0:  # 2 x low
            if "attention" in self.dimension.axis:
                return "negative and not in control"
            if "aptitude" in self.dimension.axis:
                return "negative and forceful"
        elif self.emotional_flow == 0: # low + high
            if "attention" in self.dimension.axis:
                return "negative and forceful"

            if "aptitude" in self.dimension.axis:
                return "negative and not in control"
        else:  # 2 x high
            if "aptitude" in self.dimension.axis:
                return "caring"
            if "sensitivity" in self.dimension.axis:
                return "negative and not in control"
            if "pleasantness" in self.dimension.axis:
                return "quiet positive"

    @property
    def base_emotion(self):
        # TODO science this
        return None

    @property
    def parent_emotion(self):
        # TODO science this
        return None

    @property
    def opposite_emotion(self):
        composite_emotion = OPPOSITE_EMOTIONS_NAMES.get(self.name)
        if composite_emotion:
            e = CompositeEmotion(composite_emotion)
            d = CompositeEmotionalDimension()
            for emotion in COMPOSITE_EMOTIONS_NAMES[composite_emotion]:
                emo = Emotion(emotion)
                for dim in HOURGLASS_OF_EMOTIONS:
                    if emotion in HOURGLASS_OF_EMOTIONS[dim]:
                        emo.dimension = DIMENSIONS[dim]
                e.components.append(emo)
                d.components.append(emo.dimension)
                d.axis.append(emo.dimension.axis)
                e.dimension = d
            return e
        else:
            return None

    @property
    def emotional_flow(self):
        # TODO science this instead of eye balling
        total = 0
        for emotion in self.components:
            total += abs(emotion.emotional_flow)

        return total / len(self.components)

    @property
    def is_composite(self):
        return True

    @property
    def equivalent_feeling(self):

        from emotion_data.feelings import FEELINGS_TO_EMOTION_MAP, FEELINGS
        for feel in FEELINGS_TO_EMOTION_MAP:
            #print(self.components[0].name, self.components[1].name)
            feel = feel.lower()
            if self.components[0].name in [f.lower() for f in FEELINGS_TO_EMOTION_MAP[feel]] and self.components[1].name in [f.lower() for f in FEELINGS_TO_EMOTION_MAP[feel]]:
                return FEELINGS[feel]
        return None

    def __repr__(self):
        return "CompositeEmotionObject:" + self.name


class CompositeEmotionalDimension(EmotionalDimension):
    def __init__(self):
        EmotionalDimension.__init__(self)
        self.components = []  # list of dimension objects
        self.axis = []

    def __repr__(self):
        return "CompositeDimensionObject:" + self.name
