from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    options = models.TextField(blank=True)
    correct_answer = models.CharField(max_length=255)
    difficulty_level = models.CharField(max_length=50)


class QuestionPaper(models.Model):
    title = models.CharField(max_length=255)
    duration = models.IntegerField()
    total_marks = models.IntegerField()
    questions = models.ManyToManyField(Question, related_name='question_papers')