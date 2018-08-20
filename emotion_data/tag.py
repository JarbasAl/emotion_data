import requests

# DO NOT abuse this, meant for dev purposes, you should use the official api not hijack the demo site

def tag(text, lang="en-us"):
    try:
        data = {"lang_code": lang, "text":text, "api_type": "emotion"}
        return requests.post("https://www.paralleldots.com/api/demos", data).json()["emotion"]["probabilities"]
    except:
        return {}


def test():
    TEST_SENTENCES = ['I love mom\'s cooking', #happy
                      'I love how you never reply back..', # sarcasm
                      'I love cruising with my homies', # excited
                      'I love messing with yo mind!!', # fear
                      'I love you and now you\'re just gone..', #sad
                      'This is shit', # angry
                      'This is the shit'] # excited
    for t in TEST_SENTENCES:
        print(tag(t))

