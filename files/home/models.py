from django.db import models

# Create your models here.
class Profile(models.Model):
    username=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    bio=models.CharField(max_length=150)
    location=models.CharField(max_length=100)
    socialaccount1=models.CharField(max_length=50)
    socialaccount2=models.CharField(max_length=50)
    socialaccount3=models.CharField(max_length=50)
    def __str__(self):
        return self.username
class Uploading(models.Model):
    username=models.CharField(max_length=50)
    file=models.FileField(upload_to="files",max_length=1000,default=None,null=True)
    def __str__(self):
        return self.username

