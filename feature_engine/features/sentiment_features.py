# imports
import numpy as np
from transformers import pipeline
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax


#for feature #1 (get_sentiment)
MODEL  = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

#for feature #2 (get_sentiment_1)
classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", return_all_scores=True)

"""
Primary Sentiment Analysis feature:

Grades each instance of the dataset on a pos/neu/neg probabilistic scale using HuggingFace's pretrained ROBERTA ML model. 
"""
def get_sentiment(text):
    
    #Just so I know it's running!
    print(text)

    encoded = tokenizer(text, return_tensors='pt')
    output = model(**encoded)

    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    # sample output format
    return({'positive': scores[2], 'negative': scores[0], 'neutral': scores[1]})


"""
Emotion Sentiment Analysis feature:

Grades each instance of the dataset on a scale of emotion from anger/disgust/fear/joy/neutral/sadness/surprise.
Uses HuggingFace pretrained model.
"""
def get_sentiment_1(text):
    output = classifier(text)
    maxRating = 0.0
    eLabel = ''

    for label in output[0]:
        if label['score'] > maxRating:
            maxRating = label['score']
            eLabel = label['label']
    
    return(eLabel)


