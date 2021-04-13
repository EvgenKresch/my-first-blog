from django.urls import path
from . import views

urlpatterns = [
    path('', views.questions_list, name='questions_list'),

]