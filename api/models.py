from django.db import models

class FizzBuzz(models.Model):
  fizzbuzz_id = models.BigAutoField(primary_key=True)
  useragent = models.CharField(max_length=255)
  creation_date = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
  message = models.CharField(max_length=255)

  class Meta:
    ordering = ['creation_date']

  def __str__(self):
    return self.message