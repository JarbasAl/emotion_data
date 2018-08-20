# Emotion Data

structured data to work with emotions

this project was made for use with [LILACS](https://github.com/JarbasAl/LILACS/)


# Emotion Dyads

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


dyads are represented by a DyadObject

    from emotion_data import DYADS
    
    print(DYADS)
    
    """ 
    {'aptitude': DyadObject:surprise, 'attention': DyadObject:trust, 'pleasentness': DyadObject:fear, 'sensitivity': DyadObject:joy}
    """

you can look up the dyad for an emotion

    from emotion_data import DYADS_MAP
    
    dyad = DYADS_MAP.get("anger")
    if dyad:
        print(dyad.type)
        print(dyad.basic_emotion)
        print(dyad.basic_opposite)
        print(dyad.mild_emotion)
        print(dyad.mild_opposite)
        print(dyad.intense_emotion)
        print(dyad.intense_opposite)
        
    """
    pleasentness
    fear
    anger
    apprehension
    annoyance
    terror
    rage
    """

# Emotion Types


The emotion annotation and representation language (EARL) proposed by the Human-Machine Interaction Network on Emotion (HUMAINE) classifies 48 emotions.


    from emotion_data import HUMAINES_MAP
    
    import pprint
    
    pprint.pprint(HUMAINES_MAP)
    
    """
    {'agitation': ['Stress', 'Shock', 'Tension'],
     'caring': ['affection', 'empathy', 'friendliness', 'love'],
     'negative and forceful': ['anger',
                               'annoyance',
                               'contempt',
                               'disgust',
                               'irritation'],
     'negative and not in control': ['Anxiety',
                                     'Embarrassment',
                                     'fear',
                                     'Helplessness',
                                     'Powerlessness',
                                     'Worry'],
     'negative and passive': ['boredom',
                              'despair',
                              'disappointment',
                              'hurt',
                              'sadness'],
     'negative thoughts': ['Pride',
                           'Doubt',
                           'Envy',
                           'Frustration',
                           'Guilt',
                           'Shame'],
     'positive and lively': ['Amusement',
                             'Delight',
                             'Elation',
                             'Excitement',
                             'Happiness',
                             'Joy',
                             'Pleasure'],
     'positive thoughts': ['Courage', 'Hope', 'Humility', 'Satisfaction', 'Trust'],
     'quiet positive': ['Calmness',
                        'Contentment',
                        'Relaxation',
                        'Relief',
                        'Serenity'],
     'reactive': ['Interest', 'Politeness', 'Surprise']
     }
    """
    
# Contrasting basic emotions

A 2009 review of theories of emotion identifies and contrasts fundamental emotions according to three key criteria for mental experiences that:

- have a strongly motivating subjective quality like pleasure or pain;
- are a response to some event or object that is either real or imagined;
- motivate particular kinds of behavior.

The combination of these attributes distinguishes emotions from sensations, feelings and moods.

|             kind             |                                       positive                                       |                                        negative                                       |
|:----------------------------:|:------------------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| Related to object properties | Interest, curiosity, enthusiasm, Attraction, desire, admiration, Surprise, amusement |     Indifference, habituation, boredom, Aversion, disgust, revulsion, Alarm, panic    |
|       Future appraisal       |                                   Hope, excitement                                   |                                  Fear, anxiety, dread                                 |
|         Event-related        |   Gratitude, thankfulness, Joy, elation, triumph, jubilation, Patience, Contentment  | Anger, rage, Sorrow, grief, frustration, disappointment, Discontentment, restlessness |
|        Self-appraisal        |                                   Humility, modesty                                  |                                    Pride, arrogance                                   |
|            Social            |                                   Charity, Sympathy                                  |                  Avarice, greed, miserliness, envy, jealousy, cruelty                 |
|           Cathected          |                                         love                                         |                                          hate                                         |





    from emotion_data import EMOTION_KIND_MAP
    
    import pprint
    
    pprint.pprint(EMOTION_KIND_MAP)
    
    """
    {'cathected': ['love', 'hate'],
     'event related': ['gratitude',
                       'thankfulness',
                       'anger',
                       'rage',
                       'joy',
                       'elation',
                       'triumph',
                       'jubilation',
                       'sorrow',
                       'grief',
                       'patience',
                       'frustration',
                       'disappointment',
                       'contentment',
                       'discontentment',
                       'restlessness'],
     'future appraisal': ['hope', 'excitement', 'fear', 'anxiety', 'dread'],
     'related to object properties': ['interest',
                                      'curiosity',
                                      'enthusiasm',
                                      'indifference',
                                      'habituation',
                                      'boredom',
                                      'attraction',
                                      'desire',
                                      'admiration',
                                      'aversion',
                                      'disgust',
                                      'revulsion',
                                      'surprise',
                                      'amusement',
                                      'alarm',
                                      'panic'],
     'self appraisal': ['humility', 'modesty', 'pride', 'arrogance'],
     'social': ['charity',
                'sympathy',
                'avarice',
                'greed',
                'miserliness',
                'envy',
                'jealousy',
                'cruelty']}
    """


# Emotion hierarchy
    
Some emotions are considered specialized kinds of other emotion

A tree-structured list of emotions was described in Shaver et al. (1987), and also featured in Parrott (2001).

    from emotion_data import EMOTION_TREE

    import pprint
    
    pprint.pprint(EMOTION_TREE)
    
    """
    {'anger': [{'disgust': ['revulsion', 'contempt', 'loathing'],
                'envy': ['jealousy'],
                'exasperation': ['frustration'],
                'irritability': ['aggravation',
                                 'agitation',
                                 'annoyance',
                                 'grouchy',
                                 'grumpy',
                                 'crosspatch'],
                'rage': ['anger',
                         'outrage',
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
                               'joy',
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
              'optimism': ['eagerness', 'hope'],
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
               'lust': ['desire', 'passion', 'infatuation']}],
     'sadness': [{'disappointment': ['dismay', 'displeasure'],
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
                  'shame': ['guilt', 'regret', 'remorse'],
                  'suffering': ['agony', 'anguish', 'hurt'],
                  'sympathy': ['pity', 'mono no aware']}],
     'surprise': [{'amazement': [], 'astonishment': []}]}
    """


# Emotion Objects

Emotions are represented by emotion objects

    """
    class Emotion(object):
        def __init__(self):
            self.name = ""
            self.intensity = "mild"  # mild, basic, intense
            self.is_primary = False
            self.is_secondary = False
            self.is_tertiary = False
            self.valence = 0 #-1 negative, 0 neutral, 1, positive
            self.kind = ""  # Related to object properties, Future appraisal, Event-related, Self-appraisal, Social, Cathected
            self.dimension = ""  # Sensitivity, Attention, Pleansantness, Aptitude
            self.emotional_flow = 0  # +3 to -3, 0 means undefined
            self.dyad = None  # EmotionDyad object
            self.opposite = ""  # opposite emotion name
            self.type = "neutral" # HUMAINES map classification if aplicable
            self.parent_emotion = None
    """
    
data for 153 emotions is available, it should be accurate but occasionally incomplete


    from emotion_data import EMOTION_NAMES, random_emotion
    import pprint
    
    
    print(len(EMOTION_NAMES))
    
    
    """
    153
    """
    
    emotion = random_emotion()
    pprint.pprint(emotion.__dict__)
    
    """
    {'dimension': 'pleasantness',
     'dyad': DyadObject:joy,
     'emotional_flow': -2,
     'intensity': 'mild',
     'is_primary': False,
     'is_secondary': False,
     'is_tertiary': True,
     'kind': '',
     'name': 'anguish',
     'opposite': 'joy',
     'parent_emotion': EmotionObject:suffering,
     'type': 'negative and passive',
     'valence': -1}
    """




# Composite Emotions 

Composite emotions formed from two sentic dimensions.

![compositedyads](https://upload.wikimedia.org/wikipedia/en/9/97/Hourglass-advancedemotions.png  "Advanced Emotions")

In general these are somewhat inaccurate and you will want to analyze the component emotions instead


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


# Lists and mapping


reference lists and mappings are also provided


    from emotion_data import POSITIVE_EMOTIONS, NEGATIVE_EMOTIONS, EMOTION_NAMES, OPPOSITE_EMOTION_MAP, EMOTION_MAP, COMPOSITE_EMOTIONS
    import pprint
       
    print(POSITIVE_EMOTIONS)
    
    """
    ['interest', 'curiosity', 'enthusiasm', 'amusement', 'attraction', 'desire', 'admiration', 'surprise', 'love', 'hope', 
    'excitement', 'gratitude', 'thankfulness', 'joy', 'elation', 'triumph', 'jubilation', 
    'patience', 'contentment', 'humility', 'modesty', 'charity', 'sympathy']
    
    """
    
    print(NEGATIVE_EMOTIONS)
    
    """ 
    ['indifference', 'habituation', 'boredom', 'aversion', 'disgust', 'revulsion', 
    'alarm', 'panic', 'fear', 'anxiety', 'dread', 'anger', 'rage', 'sorrow', 'grief', '
    frustration', 'disappointment', 'pride', 'arrogance', 'avarice', 'greed', 'miserliness', 
    'envy', 'jealousy', 'cruelty', 'hate']
    """
    

    print(EMOTION_NAMES)
    pprint.pprint(OPPOSITE_EMOTION_MAP)
    
    
    """
    
    ['sadness', 'compassion', 'apprehension', 'outrage' .... 'frivolity', 'embarrassment', 'enthusiasm']
    {'acceptance': 'boredom',
     'admiration': 'loathing',
     ....
     'trust': 'disgust',
     'vigilance': 'amazement'}
    """

    
    pprint.pprint(COMPOSITE_EMOTIONS)


    """
    
    {'aggressiveness': [('rage', 'vigilance'), ('anger', 'vigilance')],
     'anxiety': [('terror', 'vigilance'), ('fear', 'vigilance')],
     ...
     'remorse': [('grief', 'loathing'), ('sadness', 'amazement')],
     'rivalry': [('rage', 'admiration'), ('anger', 'admiration')],
     'submission': [('terror', 'admiration'), ('fear', 'admiration')]}
    """


    pprint.pprint(EMOTION_MAP)
    
    """
    {'acceptance': EmotionObject:acceptance,
     'admiration': EmotionObject:admiration,
     'adoration': EmotionObject:adoration,
     ....
    }
    """