# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class gaoxin(models.Model):
    years = models.CharField(max_length=8)
    company = models.CharField(max_length=80)
    def __str__(self):
        return self.company.encode('utf-8')