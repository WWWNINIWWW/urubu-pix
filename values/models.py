from django.db import models


class Values(models.Model):
    user_id = models.IntegerField(unique=True,null=False)
    value = models.DecimalField(default=0.00,decimal_places=2,max_digits=20)
    modified_at = models.DateTimeField(auto_now=True)
    last_income = models.DateTimeField(auto_now_add=True)