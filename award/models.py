from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=50)
    image = CloudinaryField('image')
    description =models.TextField(max_length=500)
    link =

class Profile(models.Model):
    profile_photo =
    bio =
    posts =
    contact =