from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Сategory(models.Model):
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Question(models.Model):
    category = models.ForeignKey(Сategory, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #answer = models.OneToOneField(Answer, on_delete=models.CASCADE, null=True)
    text = models.TextField()

    def __str__(self):
        return self.text


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text


class Answer(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='answer', null=True)
    def __str__(self):
        return self.text
