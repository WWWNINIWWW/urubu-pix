from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255)
    #value = models.DecimalField(default=0.00,decimal_places=2,max_digits=20)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
