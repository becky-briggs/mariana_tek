from django.test import TestCase
from ..models import FizzBuzz


class FizzBuzzTest(TestCase):
  """
  Test module for FizzBuzz model
  """
  def setUp(self):
    self.message1 = 'Message #1'
    self.message2 = 'Message #2'
    FizzBuzz.objects.create(message=self.message1)
    FizzBuzz.objects.create(message=self.message2)

  def test_fizzbuzz_model(self):
    fizzbuzz1 = FizzBuzz.objects.get(message=self.message1)
    fizzbuzz2 = FizzBuzz.objects.get(message=self.message2)
    self.assertEqual(str(fizzbuzz1), self.message1)
    self.assertEqual(str(fizzbuzz2), self.message2)
