

from emotion_data import get_emotion
import pprint

emotion = get_emotion("aggressiveness")
if emotion.is_composite:
    pprint.pprint(emotion.__dict__)

"""

{'components': [EmotionObject:anger, EmotionObject:vigilance],
 'dimension': '',
 'dyad': None,
 'emotional_flow': 0,
 'intensity': 'intense',
 'is_primary': True,
 'is_secondary': False,
 'is_tertiary': False,
 'kind': 'composite',
 'name': 'aggressiveness',
 'opposite': '',
 'parent_emotion': None,
 'type': 'neutral',
 'valence': 0}
"""
