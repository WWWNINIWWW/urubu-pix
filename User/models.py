from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    user_id = models.IntegerField(unique=True,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
