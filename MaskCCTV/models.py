from django.db import models

# Create your models here.
class UserInfo(models.Model):
    UserID= models.CharField(max_length=10,null=False)
    UserPWD= models.CharField(max_length=10,null=False)
