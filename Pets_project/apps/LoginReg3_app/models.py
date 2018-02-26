# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt

# Create your models here.
NAME_REGEX = re.compile(r"(^[a-zA-Z\-]+$)")
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
PASSWORD_REGEX = re.compile(r"\d.*[A-Z]|[A-Z].*\d")  ####at least one capitol letter and number

class UserManager(models.Manager):
    def createUser(self, postData):
        newUser = self.create(
            first_name = postData['first_name'],
            last_name = postData['last_name'],
            email = postData['email'],
            password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        )
        return newUser


    def validateRegister(self, postData):
        results = {'status':True, 'errors':[]}

        ################## Name validation
        if len(postData['first_name']) < 2 or len(postData['last_name']) <2:
            results['status'] = False
            results['errors'].append('Names must be more than 2 characters')
        else: 
            if re.match(NAME_REGEX, postData['first_name']) == None or re.match(NAME_REGEX, postData['last_name']) == None:
                results['status'] = False
                results['errors'].append('Names may not contain any special characters except dashes: -')
        
        ################## Email validation
        if len(postData['email']) < 1:
            results['status'] = False
            results['errors'].append('Please enter email')
        else:
            if re.match(EMAIL_REGEX, postData['email']) == None:
                results['status'] = False
                results['errors'].append('Invalid email')
            if len(self.filter(email = postData['email'])) > 0:
                results['status'] =  False
                results['errors'].append('Email already in use')

        ################## Password validation
        if len(postData['password']) < 8:
            results['status'] = False
            results['errors'].append('Passwords must be at least 8 characters long')
        if re.match(PASSWORD_REGEX, postData['password']) == None:
            results['status'] = False
            results['errors'].append('Passwords must contain at least one capitol letter and one number')
        if postData['password'] != postData['c_password']:
            results['status'] = False
            results['errors'].append('Passwords do not match')
        
        return results


    def validateLogin(self, postData):
        results = {'status' : True, 'errors' : [], 'user' : None}

        if re.match(EMAIL_REGEX, postData['email']) == None:
                results['status'] = False
                results['errors'].append('Invalid email')
        else:
            if len(self.filter(email = postData['email'])) < 1:
                results['status'] =  False
                results['errors'].append('Incorrect email or password')
            else:
                results['user'] = self.filter(email = postData['email'])[0]
                if not bcrypt.checkpw(postData['password'].encode(), results['user'].password.encode()):
                    results['status'] =  False
                    results['errors'].append('Incorrect email or password')

        return results

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()