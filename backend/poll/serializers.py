from rest_framework import serializers
from .models import Poll, Choice

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id','choice_text', 'votes']

class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True)
    #date = serializers.DateField(format='%Y-%m-%d')

    class Meta:
        model = Poll
        fields = ['id','date','name','choices']
