# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
# Create your models here.

EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
USERNAME_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+$)")
NAME_REGEX = re.compile(r"(^[a-zA-Z\-]+$)") ##allows for combined first and last names

class UserManager(models.Manager):
    def createUser(self, postData):
        self.create(
            first_name = postData['first_name'],
            last_name = postData['last_name'],
            username = postData['username'],
            email = postData['email'],
            password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            )

    def validate_reg(self, postData):
        results ={'errors':False, 'messages': []}

        ####### Name Validation
        if len(postData['first_name']) < 2 or len(postData['last_name']) < 2:
            results['errors'] = True
            results['messages'].append('Names must be more than 2 characters') 
        else:
            if re.match(NAME_REGEX, postData['first_name']) == None or re.match(NAME_REGEX, postData['last_name'])== None:
                results['errors'] = True
                results['messages'].append('Names may not contain special characters (except - )')

        ####### Username Validation
        if len(postData['username']) < 5:
            results['errors'] = True
            results['messages'].append('Username must be more than 5 characters') 
        else:
            if re.match(USERNAME_REGEX, postData['username']) == None:
                results['errors'] = True
                results['messages'].append('Invalid Username(Special Characters)')
            
            if len(User.objects.filter(username=postData['username'])) > 0:
                results['errors'] = True
                results['messages'].append('Username already in use')

        ####### Email Validation
        if re.match(EMAIL_REGEX, postData['email']) == None:
            results['errors'] = True
            results['messages'].append('Invalid email')
        
        if len(User.objects.filter(username=postData['email'])) > 0:
            results['errors'] = True
            results['messages'].append('Email already in use')

        ####### Password Validation
        if len(postData['password']) < 7:
            results['errors'] = True
            results['messages'].append('Passwords must be 8 or more characters') 
        
        if postData['password'] != postData['c_password']:
            results['errors'] = True
            results['messages'].append('Passwords must be 8 or more characters') 
        
        return results

    def validate_login(self, postData):
        results ={'errors':False, 'messages': [], 'user': None}

        ####### Email Validation
        if re.match(EMAIL_REGEX, postData['email']) == None:
            results['errors'] = True
            results['messages'].append('Invalid email')
        
        if len(self.filter(email=postData['email'])) < 1:
            
            results['errors'] = True
            results['messages'].append('Incorrect email or password')
        else:
            results['user'] = self.filter(email = postData['email'])[0]
            
        ####### Password Validation
            if not bcrypt.checkpw(postData['password'].encode(), results['user'].password.encode()):
                results['errors'] = True
                results['messages'].append('Incorrect email or password') 
        
        return results
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()