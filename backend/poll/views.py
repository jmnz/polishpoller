from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Poll, Choice
from .serializers import PollSerializer, ChoiceSerializer

class PollDetailView(APIView):
    """
    A view that returns a specific poll by its id, including its choices.
    """

    def get(self, request, pk, format=None):
        try:
            poll = Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            return Response({'error': 'Poll not found'}, status=status.HTTP_404_NOT_FOUND)

        # Retrieve the choices associated with the poll
        choices = Choice.objects.filter(poll=poll)

        # Serialize both the poll and its associated choices
        poll_serializer = PollSerializer(poll)
        choices_serializer = ChoiceSerializer(choices, many=True)

        # Combine the serialized data into a single response
        response_data = {
            'poll': poll_serializer.data,
            'choices': choices_serializer.data
        }

        return Response(response_data)
