import requests

# https://github.com/bfelbo/DeepMoji/blob/master/emoji_overview.png?raw=true
# https://www.webfx.com/tools/emoji-cheat-sheet/
# https://github.com/carpedm20/emoji
EMOJI_MAP = {
    0: ":joy:",
    1: ":unamused:",
    2: ":weary:",
    3: ":sob:",
    4: ":heart_eyes:",
    5: ":pensive:",
    6: ":ok_hand:",
    7: ":relaxed:",
    8: ":heart:",
    9: ":smirk:",
    10: ":grin:",
    11: ":notes:",
    12: ":flushed:",
    13: ":100:",
    14: ":sleeping:",
    15: ":relieved:",
    16: ":blush:",
    17: ":raised_hands:",
    18: ":two_hearts:",
    19: ":expressionless:",
    20: ":sweat_smile:",
    21: ":pray:",
    22: ":confused:",
    23: ":kissing_heart:",
    24: ":green_heart:",  # TODO same as 8 ?
    25: ":neutral_face:",
    26: ":information_desk_person:",
    27: ":disappointed:",
    28: ":see_no_evil:",
    29: ":tired_face:",
    30: ":v:",
    31: ":sunglasses:",
    32: ":rage:",
    33: ":+1:",
    34: ":cry:",
    35: ":sleepy:",
    36: ":stuck_out_tongue_closed_eyes:",
    37: ":triumph:",
    38: ":hand:",
    39: ":mask:",
    40: ":wave:",
    41: ":eyes:",
    42: ":gun:",
    43: ":persevere:",
    44: ":smiling_imp:",
    45: ":sweat:",
    46: ":broken_heart:",
    47: ":yellow_heart:",  # TODO same as 8?
    48: ":headphones:",
    49: ":speak_no_evil:",
    50: ":wink:",
    51: ":skull:",
    52: ":confounded:",
    53: ":smile:",
    54: ":stuck_out_tongue_winking_eye:",
    55: ":angry:",
    56: ":no_good:",
    57: ":muscle:",
    58: ":fist:",
    59: ":purple_heart:",
    60: ":sparkling_heart:",
    61: ":blue_heart:",
    62: ":grimacing:",
    63: ":sparkles:"
}


# http://kt.ijs.si/data/Emoji_sentiment_ranking/
# TODO
EMOJI_SENTIMENT = {}


# DO NOT abuse this, meant for dev purposes, you should deploy your own deepmoji not hijack the demo site

def get_emoji_scores(text):
    params = {"q": text}
    emojis = {}
    try:
        scores = requests.get("https://deepmoji.mit.edu/api/", params=params).json()["scores"]
        for idx, score in enumerate(scores):
            if score:
                emojis[idx] = score
    except:
        pass
    return emojis


def get_emojis(text):
    params = {"q": text}
    emojis = {}
    try:
        scores = requests.get("https://deepmoji.mit.edu/api/", params=params).json()["scores"]
        for idx, score in enumerate(scores):
            if score:
                emojis[idx] = score
        scores = sorted(emojis, key=lambda k: emojis[k])
        scores.reverse()
        return [EMOJI_MAP[s] for s in scores]
    except:
        return []

