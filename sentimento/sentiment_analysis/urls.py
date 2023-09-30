from django.urls import path
from .views import SentimentAnalysisAPIView

urlpatterns = [
    path('sentiment/', SentimentAnalysisAPIView.as_view(), name='sentiment_analysis_api'),
]