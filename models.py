# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
# Create your models here.

class students(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
