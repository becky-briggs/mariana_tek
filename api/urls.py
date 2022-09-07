from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
  path('fizzbuzz/', views.FizzBuzzList.as_view(), name='fizzbuzz-list'),
  path('fizzbuzz/<int:pk>/', views.FizzBuzzDetail.as_view(), name='fizzbuzz-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
