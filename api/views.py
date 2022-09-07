from rest_framework.response import Response
from rest_framework import generics
from .models import FizzBuzz
from .serializers import FizzBuzzSerializer


class FizzBuzzList(generics.ListCreateAPIView):
  """
  get:
  Lists all fizzbuzz objects.

  post:
  Creates a new fizzbuzz object.
  """

  queryset = FizzBuzz.objects.all()
  serializer_class = FizzBuzzSerializer

  def perform_create(self, serializer):
    # Extract useragent value from the request.
    serializer.save(useragent=self.request.META['HTTP_USER_AGENT'])

class FizzBuzzDetail(generics.RetrieveAPIView):
  """
  Retrieves a single fizzbuzz object.
  """
  queryset = FizzBuzz.objects.all()
  serializer_class = FizzBuzzSerializer
