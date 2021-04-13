from django.shortcuts import render
from .models import Question, Сategory,Answer,Comment


# Create your views here.

def questions_list(request):
    questions = Question.objects.all()
    return render(request, 'questions_list.html', {'questions': questions})
