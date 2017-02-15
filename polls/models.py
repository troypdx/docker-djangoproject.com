import datetime

from django.db import models
from django.utils import timezone

"""
Poll app models define the database schema. With this small bit of model code Django is able to:
   * Create a database schema (CREATE TABLE statements) for this app.
   * Create a Python database-access API for accessing Question and Choice objects.
"""


class Question(models.Model):
    """
    Question model: question and publication date
    """

    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    """
    Choice model: text of the choice and a vote tally. Choice is associated with a Question.
    Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.
    """

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        # __str__ methods make object representations better in interactive prompts and admin interface
        return self.choice_text
