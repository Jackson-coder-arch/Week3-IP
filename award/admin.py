from django.contrib import admin
from .models import Profile, Project, Rating, Review
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display =('user',)

@admin.register(Project)
class Project(admin.ModelAdmin):
    search_fields = ['name','image', 'description','link']

    class Meta:
        model = Project

@admin.register(Rating)
class Rating(admin.ModelAdmin):
    pass

@admin.register(Review)
class Review(admin.ModelAdmin):
    pass
