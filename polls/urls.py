from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('detail/<question_id>', views.detail),
    path('results/<question_id>', views.results),
    path('vote/<question_id>', views.vote),
]
