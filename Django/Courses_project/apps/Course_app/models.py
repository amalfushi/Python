# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class CourseManager(models.Manager):
    def validate(self, postData):
        errors = []
        if len(postData['name']) < 1:
            errors.append('Name is required')
        if len(postData['description']) < 1:
            errors.append('Description is required')
        if len(postData['description']) > 301:
            errors.append('Descriptions must be under 300 characters')
        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    objects=CourseManager()