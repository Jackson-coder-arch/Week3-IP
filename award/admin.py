from django.contrib import admin

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display =('user', 'name',)

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
