from nltk.sentiment import SentimentIntensityAnalyzer

import nltk
nltk.download('vader_lexicon')
from dataclasses import dataclass

@dataclass
class Sentiment:
    negative: float
    neuter: float
    positive: float
    compound: float

    @classmethod
    def from_sentiment_prediction(cls, sentiment_prediction: dict[str, float]) -> "Sentiment":
        negative = sentiment_prediction["neg"]
        neuter = sentiment_prediction["neu"]
        positive = sentiment_prediction["pos"]
        compound = sentiment_prediction["compound"]

        instance = Sentiment(negative=negative, neuter=neuter, positive=positive, compound=compound)

        return instance

class SentimentAnalysisService:
    sia =  SentimentIntensityAnalyzer()

    @classmethod
    def get_sentiment(cls, text: str) -> Sentiment:
        sentiment_prediction = cls.sia.polarity_scores(text)
        return Sentiment.from_sentiment_prediction(sentiment_prediction)
