# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.TextField(max_length = 50)
    text = models.TextField(max_length = 300, blank = True, null = True)
    time_created = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now = True)


    def __str__(self):
        return(self.title)