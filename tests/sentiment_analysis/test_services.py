from sentimento.sentiment_analysis.services import SentimentAnalysisService, Sentiment


class TestSentimentAnalysisService:
    def test_get_sentiment_negative(self):
        text = "This weather is quite unpleasant"
        
        sentiment = SentimentAnalysisService.get_sentiment(text)

        assert isinstance(sentiment, Sentiment)
        assert sentiment.negative > sentiment.positive
        assert sentiment.compound < 0

    def test_get_sentiment_neuter(self):
        text = "Today is wednesday"
        
        sentiment = SentimentAnalysisService.get_sentiment(text)

        assert isinstance(sentiment, Sentiment)
        assert sentiment.neuter > sentiment.negative
        assert sentiment.neuter > sentiment.positive

    def test_get_sentiment_positive(self):
        text = "You look great on this sweater"
        
        sentiment = SentimentAnalysisService.get_sentiment(text)

        assert isinstance(sentiment, Sentiment)
        assert sentiment.positive > sentiment.negative
        assert sentiment.compound > 0
