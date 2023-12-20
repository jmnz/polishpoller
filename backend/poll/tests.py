from django.test import TestCase
from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer
from .views import PollDetailView
from collections import OrderedDict
from rest_framework.response import Response
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.utils import timezone



class SerializerTest(TestCase):
    def setUp(self):
        self.poll = Poll.objects.create(name='Test Poll', date=timezone.now())
        self.choice = Choice.objects.create(choice_text='Choice 1', votes=0, poll=self.poll)

    def test_choice_serializer(self):
        cserializer = ChoiceSerializer(instance=self.choice)
        expected_data1 = {'id': self.choice.id, 'choice_text': 'Choice 1', 'votes': 0}
        self.assertEqual(cserializer.data, expected_data1)

    def test_poll_serializer(self):
        pserializer = PollSerializer(instance=self.poll)
        expected_data2 = {
            'id': self.poll.id,
            'date': str(self.poll.date),
            'name': 'Test Poll',
            'choices': [ChoiceSerializer(self.choice).data]
        }
        self.assertEqual(pserializer.data, expected_data2)


class PollDetailViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create sample polls and choices
        self.poll1 = Poll.objects.create(name='Poll 1')
        self.choice1a = Choice.objects.create(choice_text='Choice 1A', poll=self.poll1)
        self.choice1b = Choice.objects.create(choice_text='Choice 1B', poll=self.poll1)

        self.poll2 = Poll.objects.create(name='Poll 2')
        self.choice2a = Choice.objects.create(choice_text='Choice 2A', poll=self.poll2)
        self.choice2b = Choice.objects.create(choice_text='Choice 2B', poll=self.poll2)

        self.poll3 = Poll.objects.create(name='Poll 3')
        self.choice3a = Choice.objects.create(choice_text='Choice 3A', poll=self.poll3)
        self.choice3b = Choice.objects.create(choice_text='Choice 3B', poll=self.poll3)

        self.poll4 = Poll.objects.create(name='Poll 4')

    def test_get_poll_with_choices(self):
        # Test retrieving a specific poll with its choices
        for poll, choices in [
            (self.poll1, [self.choice1a, self.choice1b]),
            (self.poll2, [self.choice2a, self.choice2b]),
            (self.poll3, [self.choice3a, self.choice3b]),
        ]:
            url = reverse('poll-detail', args=[poll.id])
            response = self.client.get(url, format='json')

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            expected_data = {
                'poll': PollSerializer(poll).data,
                'choices': ChoiceSerializer(choices, many=True).data
            }
            self.assertEqual(response.data, expected_data)

    def test_get_nonexistent_poll(self):
        # Test retrieving a poll that doesn't exist
        url = reverse('poll-detail', args=[999])  # Assuming 999 doesn't exist
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data, {'error': 'Poll not found'})

    # Add more test cases for other scenarios as needed

    def test_get_poll_with_no_choices(self):
        # Test retrieving a specific poll with no choices
        url = reverse('poll-detail', args=[self.poll4.id])
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {
            'poll': PollSerializer(self.poll4).data,
            'choices': [],
        }
        self.assertEqual(response.data, expected_data)
