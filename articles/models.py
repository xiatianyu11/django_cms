# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django.utils import  timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50)
    source = models.CharField(max_length=200)
    updateTime = models.DateTimeField()
    readCount = models.IntegerField(default=0)
    state = models.CharField(max_length=1)

    def __str__(self): # only if you need to support Python 2
        return self.title
