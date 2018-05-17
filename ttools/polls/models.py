from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=250)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Profile(models.Model):
    """
    1 profile for 1 user
    mdoels.CASCADE means when you delete a user, the profile will be deleted too.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, default="My bio")

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.author} on question - {self.question} - {self.text}"