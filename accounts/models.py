# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Account(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    user = models.OneToOneField(User)
    nickname = models.CharField(max_length=20)
    avatar = models.ImageField(upload_to='avatar')
    bdc_quota = models.IntegerField(default=50)

    def __str__(self):
        return self.user.username

    def save(self, **kwargs):
        if self not in Account.objects.all():
            self.id = self.user.id
        super(Account, self).save(**kwargs)
