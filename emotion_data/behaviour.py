from emotion_data.emotions import EMOTIONS

BEHAVIOUR_NAMES = {
    "protection": {
        "purpose": "Withdrawal, retreat",
        "activated_by": ["fear", "terror"]
    },
    "destruction": {
            "purpose": "Elimination of barrier to the satisfaction of needs",
            "activated_by": ["anger", "rage"]
        },
    "incorporation": {
            "purpose": "Ingesting nourishment",
            "activated_by": ["acceptance"]
        },
    "rejection": {
            "purpose": "Riddance response to harmful material",
            "activated_by": ["disgust"]
        },
    "reproduction": {
            "purpose": "Approach, contract, genetic exchanges",
            "activated_by": ["joy", "pleasure"]
        },
    "reintegration": {
            "purpose": "Reaction to loss of nutrient product",
            "activated_by": ["sadness", "grief"]
        },
    "exploration": {
            "purpose": "Investigating an environment",
            "activated_by": ["curiosity", "play"]
        },
    "orientation": {
            "purpose": "Reaction to contact with unfamiliar object",
            "activated_by": ["surprise"]
        }
}

REACTION_NAMES = {
    "retain or repeat": {
        "function": "gain resources",
        "cognite appraisal": "possess",
        "trigger": "gain of value",
        "base_emotion": "serenity",
        "behaviour": "incorporation"
    },
    "groom": {
        "function": "mutual support",
        "cognite appraisal": "friend",
        "trigger": "member of one's group",
        "base_emotion": "acceptance",
        "behaviour": "reproduction"
    },
    "escape": {
        "function": "safety",
        "cognite appraisal": "danger",
        "trigger": "threat",
        "base_emotion": "apprehension",
        "behaviour": "protection"
    },
    "stop": {
        "function": "gain time",
        "cognite appraisal": "orient self",
        "trigger": "unexpected event",
        "base_emotion": "distraction",
        "behaviour": "orientation"
    },
    "cry": {
        "function": "reattach to lost object",
        "cognite appraisal": "abandonment",
        "trigger": "loss of value",
        "base_emotion": "pensiveness",
        "behaviour": "reintegration"
    },
    "vomit": {
        "function": "eject poison",
        "cognite appraisal": "poison",
        "trigger": "unpalatable object",
        "base_emotion": "boredom",
        "behaviour": "rejection"
    },
    "attack": {
        "function": "destroy obstacle",
        "cognite appraisal": "enemy",
        "trigger": "obstacle",
        "base_emotion": "annoyance",
        "behaviour": "destruction"
    },
    "map": {
        "function": "knowledge of territory",
        "cognite appraisal": "examine",
        "trigger": "new territory",
        "base_emotion": "interest",
        "behaviour": "exploration"
    }
}


class Behaviour(object):
    def __init__(self, name, purpose = ""):
        self.name = name
        self.purpose = purpose
        self.activated_by = []

    def __repr__(self):
        return "BehaviourObject:" + self.name


def _get_behaviours():
    bucket = {}
    for behaviour in BEHAVIOUR_NAMES:
        data = BEHAVIOUR_NAMES[behaviour]
        b = Behaviour(behaviour)
        b.purpose = data["purpose"]
        for emo in data["activated_by"]:
            e = EMOTIONS.get(emo)
            if e:
                b.activated_by.append(e)
        bucket[behaviour] = b
    return bucket


BEHAVIOURS = _get_behaviours()


class BehavioralReaction(object):
    def __init__(self, name):
        self.name = name
        self.function = ""
        self.cognite_appraisal = ""
        self.trigger = ""
        self.base_emotion = None # emotion object
        self.behaviour = None # behaviour object

    def from_data(self, data=None):
        data = data or {}
        self.name = data.get("name") or self.name
        self.function = data.get("function", "")
        self.cognite_appraisal = data.get("cognite appraisal", "")
        self.trigger = data.get("trigger", "")
        self.base_emotion = EMOTIONS.get(data.get("base_emotion", ""))
        self.behaviour = BEHAVIOURS[data["behaviour"]]

    def __repr__(self):
        return "BehavioralReactionObject:" + self.name


def _get_reactions():
    bucket = {}
    bucket2 = {}
    for reaction in REACTION_NAMES:
        data = REACTION_NAMES[reaction]

        r = BehavioralReaction(reaction)
        r.from_data(data)
        bucket[r.name] = r
        bucket2[r.name] = r.base_emotion

    return bucket, bucket2


REACTIONS, REACTION_TO_EMOTION_MAP = _get_reactions()


if __name__ == "__main__":
    from pprint import pprint

    pprint(BEHAVIOURS)
    pprint(REACTIONS)
    pprint(REACTION_TO_EMOTION_MAP)