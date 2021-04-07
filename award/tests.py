from django.test import TestCase
from .models import *

# Create your tests here.
class Project(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='jack')
        self.project =Project.objects.create(id=1,name='test project',image='default.jpg',description='descr',
        user=self.user,link='https://instapicts.herokuapp.com/'
        

    def test_instance(self):
        self.assertTrue(isinstance(self.project,Project))

    def test_save_project(self):
        self.project.save_project()
        project = Project.objects.all()
        self.assertTrue(len(project) > 0)

    def test_get_projects(self):
        self.project.save()
        project = Project.all_projects('test')
        self.assertTrue(len(project) > 0)


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='jack',password='jack')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self,user,User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()


class RatingTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='jack')
        self.project =Project.objects.create(id=1,name='test project',image='default.jpg',description='descr',
        
        self.rating = Rating.objects.create(id=1,usability=7,content=8,user=self.user,project=self.project)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_get_post_rating(self, id):
        self.rating.save()
        rating = Rating.get_ratings(post_id=id)
        self.assertTrue(len(rating) == 1)
 
