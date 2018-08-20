import requests

# DO NOT abuse this, meant for dev purposes, you should use the official api not hijack the demo site


def tag(text, lang="en-us"):
    try:
        data = {"lang_code": lang, "text":text, "api_type": "emotion"}
        return requests.post("https://www.paralleldots.com/api/demos", data).json()["emotion"]["probabilities"]
    except:
        return {}

