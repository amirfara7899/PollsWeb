from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('detail/<question_id>', views.detail),
    path('<question_id>/results', views.results),
    path('<question_id>/vote', views.vote),
]
