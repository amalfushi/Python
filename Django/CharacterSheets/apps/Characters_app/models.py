# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Class(models.Model):
    modStr = models.IntegerField(default=0)
    modDex = models.IntegerField(default=0)
    modCon = models.IntegerField(default=0)
    modInt = models.IntegerField(default=0)
    modWis = models.IntegerField(default=0)
    modCha = models.IntegerField(default=0)
    
class StatBlock(models.Model):
    strength = models.IntegerField(default=10)
    dexterity = models.IntegerField(default=10)
    constitution = models.IntegerField(default=10)
    intelligence = models.IntegerField(default=10)
    wisdom = models.IntegerField(default=10)
    charisma = models.IntegerField(default=10)

class Character(models.Model):
    name = models.CharField(max_length=255)
    stats = models.ForeignKey(StatBlock, related_name='characters')
    charClass = models.ForeignKey(Class, related_name='characters')
    created_at = models.DateTimeField(auto_now_add=True)