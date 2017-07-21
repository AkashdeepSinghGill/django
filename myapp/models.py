# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
class User(models.Model):
    name = models.CharField(max_length=255)
    Phone = models.CharField(max_length=30)
    has_verified_phone = models.BooleanField(default=False)
    age = models.IntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)

