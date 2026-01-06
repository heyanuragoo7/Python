from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField()
    age = models.IntegerField()
    role = models.CharField(default='user')

class Blog(models.Model):
    owner = models.ForeignKey(User, related_name='blog', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)