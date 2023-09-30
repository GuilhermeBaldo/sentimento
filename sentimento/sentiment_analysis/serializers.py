from rest_framework import serializers

class SentimentAnalysisRequestSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1000)

class SentimentAnalysisResponseSerializer(serializers.Serializer):
    negative = serializers.FloatField()
    neuter = serializers.FloatField()
    positive = serializers.FloatField()
    compound = serializers.FloatField()