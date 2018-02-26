# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..LoginReg3_app.models import User

# Create your models here.
class CommentManager(models.Manager):
    def createComment(self, postData):
        tempComment = self.create(
            comment_text = postData['newComment'],
            recipient = User.objects.get(id=postData['recipient']),
            sender = User.objects.get(id=postData['userID']),
        )
    def validateComment(self, postData):
        results ={'status': True, 'errors': []}
        
        if len(postData['newComment']) < 2:
            results['status'] = False
            results['errors'].append('Comments must be at least 2 characters')
        
class Comment(models.Model):
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    recipient = models.ForeignKey(User, related_name='recieved_comments')
    sender = models.ForeignKey(User, related_name='sent_comments')
    objects = CommentManager()