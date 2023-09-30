from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class TestSentimentAnalysisAPIView(APITestCase):

    def test_sentiment_analysis_api(self):
        url = reverse('sentiment_analysis_api')
        data = {'text': 'This is a good sentence'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.keys(), {'negative', 'neuter', 'positive', 'compound'})
