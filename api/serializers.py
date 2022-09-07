import string
from rest_framework import serializers
from .models import FizzBuzz


class FizzBuzzSerializer(serializers.ModelSerializer):
  # Set useragent field to read_only as it is extracted from the request.
  useragent = serializers.CharField(read_only=True)

  def validate(self, data):
    """
    Verify that the message contains some letters.
    """
    letters = set(string.ascii_letters)
    msg = set(data['message'])
    if msg.isdisjoint(letters):
      raise serializers.ValidationError("Message must contains letters.")
    return data

  class Meta:
    model = FizzBuzz
    fields = ('fizzbuzz_id', 'useragent', 'creation_date', 'message')
