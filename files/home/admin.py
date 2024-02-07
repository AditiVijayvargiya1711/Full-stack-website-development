from django.contrib import admin
from home.models import Profile,Uploading

# Register your models here.
myModels = [Profile, Uploading]  # iterable list
admin.site.register(myModels)
