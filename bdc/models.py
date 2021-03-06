# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Word(models.Model):
    name = models.CharField(max_length=50)
    pronunciation = models.CharField(max_length=50)
    definition = models.TextField()

    def __str__(self):
        return self.name

    def name_capitalized(self):
        return self.name.capitalize()


@python_2_unicode_compatible
class Learning(models.Model):
    user = models.ForeignKey(User)
    word = models.ForeignKey(Word)
    learning_date = models.DateField()
    review_status = models.SmallIntegerField()
    review_times = models.SmallIntegerField()

    def __str__(self):
        return '{0}\'s learning of {1}'.format(self.user.username, self.word.name)


@python_2_unicode_compatible
class Audio(models.Model):
    addresses = models.CharField(max_length=255)
