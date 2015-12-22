from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    user = models.ForeignKey(User)
    nickname = models.CharField(max_length=20)
    
