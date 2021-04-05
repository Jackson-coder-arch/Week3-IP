from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    image=CloudinaryField('image')
    description =models.TextField(max_length=500)
    link = models.CharField(max_length=300)

    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects

    class Meta:
        ordering = ["-pk"]
    
    @property

    def save_projects(self):
        self.save()
    def delete_projects(self):
        self.delete()

    def __str__(self):
        return self.projects_caption

class Profile(models.Model):
    profile_photo = CloudinaryField('image')
    bio =models.TextField(max_length= 300)
    posts = models.CharField(max_length=100)
    contact = models.EmailField

class Rating(models.Model):
    pass

class Review(models.Model):
    pass


