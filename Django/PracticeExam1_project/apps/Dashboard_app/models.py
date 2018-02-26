# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..LoginReg3_app.models import User

# Create your models here.

class CommentManager(models.Manager):
    def validateComment(self, postData):
        results ={'status': True, 'errors' : []}
        if len(postData['comment']) < 1:
            results['status'] = False
            results['errors'].append('Comments must include some text')

        # maybe check to see if the logged user is trying to comment on themselves
        return results
    
    def createComment(self, postData):
        newComment = self.create(
            comment_text=postData['comment'],
            sender = User.objects.get(id=int(postData['sender'])),
            recipient = User.objects.get(id=int(postData['recipient'])),
        )
        return newComment
        
class Comment(models.Model):
    comment_text = models.CharField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, related_name='comments_made')
    recipient = models.ForeignKey(User, related_name='recieved_comments')
    objects = CommentManager()