from django.db import models

class Transactions(models.Model):
    user_id = models.IntegerField(unique=True,null=False)
    deposit = models.DecimalField(null=False,default=0,decimal_places=2,max_digits=20)
    withdraw = models.DecimalField(null=False,default=0,decimal_places=2,max_digits=20)
    modified_at = models.DateTimeField(auto_now=True)