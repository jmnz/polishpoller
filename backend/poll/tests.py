from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer
from collections import OrderedDict




class SerializerTest(TestCase):
    def setUp(self):
        self.poll = Poll.objects.create(name='Test Poll')
        self.choice = Choice.objects.create(choice_text='Choice 1', votes=0, poll=self.poll)
        self.poll.choices.add(self.choice)

    def test_choice_serializer(self):
        cserializer = ChoiceSerializer(instance=self.choice)
        expected_data1 = {'id': 1, 'choice_text': 'Choice 1', 'votes': 0}
        print("Serialized Choice Data:", cserializer.data)
        print("Expected Choice Data:", expected_data1)

        self.assertEqual(cserializer.data, expected_data1)

    def test_poll_serializer(self):
        pserializer = PollSerializer(instance=self.poll)
        expected_data2 = {'id': 2, 'date': '2023-12-10', 'name': 'Test Poll', 'choices': [OrderedDict([('id', 2), ('choice_text', 'Choice 1'), ('votes', 0)])]}
        print("Serialized Poll Data:", pserializer.data)
        print("Expected Poll Data:", expected_data2)
        self.assertEqual(pserializer.data, expected_data2)
