from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory
from ..models import FizzBuzz
from ..serializers import FizzBuzzSerializer
from .. import views

class GetAllFizzBuzzesTest(TestCase):
  """
  Test module for GET all fizzbuzzes API
  """

  def setUp(self):
    FizzBuzz.objects.create(message='Message #1')
    FizzBuzz.objects.create(message='Message #2')
    FizzBuzz.objects.create(message='Message #3')
    FizzBuzz.objects.create(message='Message #4')

  def test_get_all_fizzbuzzes(self):
    """
    Verify we can list all fizzbuzzes.
    """
    # Using the standard RequestFactory API to create a GET request
    factory = APIRequestFactory()
    request = factory.get('/fizzbuzz/')

    # Get API response
    view = views.FizzBuzzList.as_view()
    response = view(request)
    # Get data from DB
    fizzbuzzes = FizzBuzz.objects.all()
    serializer = FizzBuzzSerializer(fizzbuzzes, many=True)
    self.assertEqual(response.data, serializer.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleFizzBuzzTest(TestCase):
  """
  Test module for GET single fizzbuzz API
  """

  def setUp(self):
    self.fizzbuzz1 = FizzBuzz.objects.create(message='Message #1')
    self.fizzbuzz2 = FizzBuzz.objects.create(message='Message #2')
    self.fizzbuzz3 = FizzBuzz.objects.create(message='Message #3')
    self.fizzbuzz4 = FizzBuzz.objects.create(message='Message #4')

  def test_get_valid_single_fizzbuzz(self):
    """
    Verify we can view a single valid fizzbuzz.
    """
    # Using the standard RequestFactory API to create a GET request
    factory = APIRequestFactory()
    request = factory.get('/fizzbuzz')

    # Get API response
    view = views.FizzBuzzDetail.as_view()
    response = view(request, pk=self.fizzbuzz3.pk)
    # Get data from DB
    fizzbuzz = FizzBuzz.objects.get(pk=self.fizzbuzz3.pk)
    serializer = FizzBuzzSerializer(fizzbuzz)
    self.assertEqual(response.data, serializer.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_get_invalid_single_fizzbuzz(self):
    """
    Verify we cannot view a single invalid fizzbuzz.
    """

    # Using the standard RequestFactory API to create a GET request
    factory = APIRequestFactory()
    request = factory.get('/fizzbuzz')

    # Get API response
    view = views.FizzBuzzDetail.as_view()
    response = view(request, pk=30)
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewFizzBuzzTest(TestCase):
  """
  Test module for POST single fizzbuzz API
  """

  def setUp(self):
    self.useragent = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko)',
                      ' Chrome/41.0.2272.118 Safari/537.36')

  def test_create_valid_fizzbuzz(self):
    """
    Verify we can create a new fizzbuzz object with a valid message.
    """

    self.valid_message = 'Message #1'
    self.valid_fizzbuzz_payload = {'message': self.valid_message}

    # Using the standard RequestFactory API to create a POST request
    factory = APIRequestFactory()
    request = factory.post('/fizzbuzz/', self.valid_fizzbuzz_payload, HTTP_USER_AGENT=self.useragent)

    # Get API response
    view = views.FizzBuzzList.as_view()
    response = view(request)

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(FizzBuzz.objects.count(), 1)
    self.assertEqual(FizzBuzz.objects.get().message, self.valid_message)

  def test_create_invalid_fizzbuzz(self):
    """
    Verify we cannot create a fizzbuzz object with no letters in the message.
    """

    self.invalid_fizzbuzz_payload = {'message': '#1'}

    # Using the standard RequestFactory API to create a POST request
    factory = APIRequestFactory()
    request = factory.post('/fizzbuzz/', self.invalid_fizzbuzz_payload, HTTP_USER_AGENT=self.useragent)

    # Get API response
    view = views.FizzBuzzList.as_view()
    response = view(request)

    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertEqual(FizzBuzz.objects.count(), 0)

  def test_create_blank_fizzbuzz(self):
    """
    Verify we cannot create a blank fizzbuzz object.
    """

    self.blank_fizzbuzz_payload = {'message': ''}

    # Using the standard RequestFactory API to create a POST request
    factory = APIRequestFactory()
    request = factory.post('/fizzbuzz/', self.blank_fizzbuzz_payload, HTTP_USER_AGENT=self.useragent)

    # Get API response
    view = views.FizzBuzzList.as_view()
    response = view(request)

    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertEqual(FizzBuzz.objects.count(), 0)
