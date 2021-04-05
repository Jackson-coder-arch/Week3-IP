from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=50)
    image=CloudinaryField('image')
    description =models.TextField(max_length=500)
    link = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    design = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    creativity = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)

    @classmethod
    def get_info(cls):
        info = cls.objects.all()
        return info

    class Meta:
        ordering = ["-pk"]
    
    @property
    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def search_project_by_name(cls, search_term):
        project = cls.objects.filter(name__icontains=search_term)
        return project

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null = True)
    profile_photo = CloudinaryField('image')
    bio =models.TextField(max_length= 300)
    posts = models.CharField(max_length=100)
    # contact = models.EmailField(max_length=30)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()



class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    Project = models.ForeignKey(Project, on_delete=models.PROTECT, related_name='likes', null=True)
    design = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    usability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], null=True)
    creativity = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    content = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])

    def save_rate(self):
        self.save()

    def delete_rate(self):
        self.delete()

    class Meta:
        db_table = 'rating'

    

class Review(models.Model):
    review = models.CharField(max_length=80, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

    class Meta:
        db_table = 'comments'
        ordering = ["-id"]



