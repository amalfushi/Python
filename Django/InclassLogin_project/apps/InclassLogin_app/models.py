# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

# Create your models here.
class UserManager(models.Manager):
    def createUser(self, postData):
        thisPassword = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        User.objects.create(
            first_name = postData['first_name'],
            last_name = postData['last_name'],
            email = postData['email'],
            password = thisPassword
        )

    def registerVal(self, postData):
        results = {'errors': [], 'status': False}

        if len(postData['first_name']) < 2:
            results['status'] = True
            results['errors'].append('First name is too short')
            
        if len(postData['last_name']) < 2:
            results['status'] = True
            results['errors'].append('Last name is too short')

        if not re.match((r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-z]+$'), postData['email']):
            results['status'] = True
            results['errors'].append('Invalid email')

        if len(postData['password']) < 3:
            results['status'] = True
            results['errors'].append('Password is too short')

        if postData['password'] != postData['c_password']:
            results['status'] = True
            results['errors'].append('Passwords do not match')

        user = self.filter(email=postData['email'])
        if len(user) > 0:
            results['status'] = True
            results['errors'].append('Email already exists')
            
        return results

    def loginVal(self, postData):
        results = {'errors': [], 'status': False, 'user': None}
        emailMatches = self.filter(email = postData['email'])

        if len(emailMatches) < 1:
            results['status'] = False
            results['errors'].append('Please check your email and password')
        else:
            results['user'] = emailMatches[0]
            if not bcrypt.checkpw(postData['password'].encode(), results['user'].password.encode()):
                results['status'] = False
                results['errors'].append('Please check your email and password')
        return results       

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()