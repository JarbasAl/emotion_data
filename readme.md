# Emotion Data
[![Donate with Bitcoin](https://en.cryptobadges.io/badge/micro/1QJNhKM8tVv62XSUrST2vnaMXh5ADSyYP8)](https://en.cryptobadges.io/donate/1QJNhKM8tVv62XSUrST2vnaMXh5ADSyYP8)
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://paypal.me/jarbasai)
<span class="badge-patreon"><a href="https://www.patreon.com/jarbasAI" title="Donate to this project using Patreon"><img src="https://img.shields.io/badge/patreon-donate-yellow.svg" alt="Patreon donate button" /></a></span>
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/JarbasAl)

read the [blog post](https://jarbasal.github.io/posts/2018/10/emotion_data/)

structured data to work with emotions

this project was made for use with [LILACS](https://github.com/JarbasAl/LILACS/), this is early work and subject to change, information bellow may be outdated


reference - https://positivepsychologyprogram.com/emotion-wheel/


# Install

    pip install numpy
    pip install emotion_data
    
    
# Plutchik's wheel of emotions

In 1980, Robert Plutchik constructed diagram of emotions visualising eight basic emotions: joy, trust, fear, surprise, sadness, disgust, anger and anticipation. 

Emotions can be mild or intense; for example, distraction is a mild form of surprise, and rage is an intense form of anger.

![dyads](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ce/Plutchik-wheel.svg/350px-Plutchik-wheel.svg.png  "dyads")

The 2012 book The Hourglass of Emotions was based on Robert Plutchik's model, but categorised the emotions into four sentic dimensions. 
It contrasted anger, anticipation, joy, and trust as positive emotions, and fear, surprise, sadness and disgust as negative.

| dimension/flow |      3     |       2      |      1     |      -1      |    -2    |     -3    |
|:--------------:|:----------:|:------------:|:----------:|:------------:|:--------:|:---------:|
|   sensitivity  |    rage    |     anger    |  annoyance | apprehension |   fear   |   terror  |
|    attention   |  vigilance | anticipation |  interest  |  distraction | surprise | amazement |
|  pleasantness  |   ecstasy  |      joy     |  serenity  |  pensiveness |  sadness |   grief   |
|    aptitude    | admiration |     trust    | acceptance |    boredom   |  disgust |  loathing |




# Feelings

Jessica Hagy wrote on her blog that Plutchik's wheel of emotions gave a demonstration on emotions, but needed more levels of intensity in the emotion combinations. 
She observed that the wheel was a Venn diagram format, and expanded the primary dyads.

Feelings are groups of two emotions, these are related but not the same thing as composite emotions


# Emotion Algebra

Based on this some new data types were created

- [dimensions](/examples/dimension_algebra.py)
- [emotions](/examples/emotion_algebra.py)
- [feelings](/examples/feeling_algebra.py)
- [composite emotions](/examples/composite_emotion_algebra.py)
