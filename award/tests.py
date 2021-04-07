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
