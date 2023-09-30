from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from sentimento.sentiment_analysis.services import SentimentAnalysisService
from sentimento.sentiment_analysis.serializers import SentimentAnalysisRequestSerializer, SentimentAnalysisResponseSerializer

class SentimentAnalysisAPIView(APIView):
    def post(self, request):
        serializer = SentimentAnalysisRequestSerializer(data=request.data)

        if serializer.is_valid():
            text = serializer.validated_data.get('text')
            sentiment = SentimentAnalysisService.get_sentiment(text)
            serializer_result = SentimentAnalysisResponseSerializer(sentiment)
            return Response(serializer_result.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)