from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    image = CloudinaryField('image')
    description =models.TextField(max_length=500)
    link =

class Profile(models.Model):
    profile_photo = CloudinaryField('image')
    bio =models.TextField(max_length= 300)
    posts = models.CharField(max_length=100)
    contact = models.EmailField

class Rating(models.Model):
    Post

class Review(models.Model):


