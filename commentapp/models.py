from django.db import models
from django.contrib.auth.models import User
from articleapp.models import Article

# Create your models here.
class Comment(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='comment', null=True)
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, related_name='comment', null=True)

    content = models.TextField(null=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)