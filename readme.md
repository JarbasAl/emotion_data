# Emotion Data

structured data to work with emotions

this project was made for use with [LILACS](https://github.com/JarbasAl/LILACS/), this is early work and subject to change, information bellow may be outdated


reference - https://en.wikipedia.org/wiki/Contrasting_and_categorization_of_emotions


# Install


    pip install emotion_data
    
    
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


you can think of dyads as "dimensions of feelings"

dyads are represented by a DyadObject, you can look up the dyad for an emotion

    from emotion_data import get_dyad
    
    dyad = get_dyad("anger")
    pprint.pprint(dyad.__dict__)
    
    """
        {'basic_emotion': 'fear',
         'basic_opposite': 'anger',
         'dimension': 'pleasentness',
         'intense_emotion': 'terror',
         'intense_opposite': 'rage',
         'mild_emotion': 'apprehension',
         'mild_opposite': 'annoyance'}
    """

composite emotions will have more than 1 dyad

        dyad = get_dyad("love")
        if isinstance(dyad, list):
            for d in dyad:
                pprint.pprint(d.__dict__)
        
        """
            {'basic_emotion': 'joy',
         'basic_opposite': 'sadness',
         'dimension': 'sensitivity',
         'intense_emotion': 'ecstasy',
         'intense_opposite': 'grief',
         'mild_emotion': 'serenity',
         'mild_opposite': 'pensiveness'}
         
        {'basic_emotion': 'trust',
         'basic_opposite': 'disgust',
         'dimension': 'attention',
         'intense_emotion': 'admiration',
         'intense_opposite': 'loathing',
         'mild_emotion': 'acceptance',
         'mild_opposite': 'boredom'}
        """

dyad may be None for some emotions (open an issue!)


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
     
        ....
     
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
     'dyad': DyadObject:sensitivity,
     'emotional_flow': 2,
     'intensity': 'mild',
     'is_primary': False,
     'is_secondary': False,
     'is_tertiary': True,
     'kind': 'event related',
     'name': 'elation',
     'opposite': 'sadness',
     'parent_emotion': EmotionObject:cheerfulness,
     'type': 'neutral',
     'valence': 1}
    """


# Feelings

Jessica Hagy wrote on her blog that Plutchik's wheel of emotions gave a demonstration on emotions, but needed more levels of intensity in the emotion combinations. 
She observed that the wheel was a Venn diagram format, and expanded the primary dyads.

Feelings are groups of two emotions, these are related but not the same thing as composite emotions


There are currently 39 feelings

  
        from emotion_data.feelings import get_feeling, random_feeling, FEELINGS_MAP
        
        print(len(FEELINGS_MAP))  # 39
        
        f = get_feeling("despair")
        pprint.pprint(f.__dict__)
        
        """
        {'dyads': [DyadObject:pleasentness, DyadObject:sensitivity],
         'emotions': [EmotionObject:fear, EmotionObject:sadness],
         'name': 'despair'}
        """
        
        f = random_feeling()
        pprint.pprint(f.__dict__)
        
        """
        {'dyads': [DyadObject:pleasentness, DyadObject:aptitude],
         'emotions': [EmotionObject:annoyance, EmotionObject:interest],
         'name': 'disfavor'}
        """
        
        pprint.pprint(FEELINGS_MAP)
        
        """
        {'acknowledgement': FeelingObject:acknowledgement,
         'acquiescence': FeelingObject:acquiescence,
         'aggressiveness': FeelingObject:aggressiveness,
        
        ...
        
         'wariness': FeelingObject:wariness,
         'zeal': FeelingObject:zeal}
         """

NOTE: Feelings and Emotions may share names:

- Love (composite emotion) = Ecstasy + Admiration
- Love (feeling) = Joy + Trust


NOTE: there may be more than 1 feeling with the same name but different dyads:

- Shame = Fear + Disgust
- Shame = Grief + Loathing


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


    from emotion_data import *
    import pprint
       
    print(DYADS)
    
    """ 
    {'aptitude': DyadObject:surprise, 'attention': DyadObject:trust, 'pleasentness': DyadObject:fear, 'sensitivity': DyadObject:joy}
    """
    
    pprint.pprint(DYADS_MAP)
    
    """
    {'acceptance': DyadObject:trust,
    
    ...
    
     'terror': DyadObject:fear,
     'trust': DyadObject:trust,
     'vigilance': DyadObject:surprise}
    """
    
    
    pprint.pprint(DIMENSION_MAP)

    """
    
    {'aptitude': ['admiration',
                  'trust',
                  'acceptance',
                  'boredom',
                  'disgust',
                  'loathing'],
     'attention': ['vigilance',
                   'anticipation',
                   'interest',
                   'distraction',
                   'surprise',
                   'amazement'],
     'pleasantness': ['ecstasy',
                      'joy',
                      'serenity',
                      'pensiveness',
                      'sadness',
                      'grief'],
     'sensitivity': ['rage',
                     'anger',
                     'annoyance',
                     'apprehension',
                     'fear',
                     'terror']}
    """

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
