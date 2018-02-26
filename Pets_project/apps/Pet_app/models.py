# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..LoginReg3_app.models import User
import re

# Create your models here.
NAME_REGEX = re.compile(r"(^[a-zA-Z\-]+$)")

class Pet(models.Model):
    name = models.CharField(max_length=255)
    kind = models.CharField(max_length=255)
    owners = models.ManyToManyField(User, related_name='pets')
    objects = PetManager()

class PetManager(models.Manager):
    def validatePet(self, postData):
        results = {'status':True, 'errors':[]}
        if len(postData['name']) <2:
            results['status'] = False
            results['errors'].append('Pet names must be longer than 2 characters')
        
        if re.match(NAME_REGEX, postData['name']):
            results['status'] = False
            results['errors'].append('Pet names cannot include special characters')

        if re.match(NAME_REGEX, postData['kind']):
            results['status'] = False
            results['errors'].append('Pet types cannot include special characters')

    def createPet(self, postData):
        newPet = self.create(
            name = postData['name'],
            kind = postData['kind'],
            owner = User.objects.get(id=postData['ownerID'])
        )