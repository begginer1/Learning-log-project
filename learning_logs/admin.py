from django.contrib import admin

# Register your models here.
from .models import Topic,Entry # . tell to look in same directory

admin.site.register(Topic)
#The code admin.site.register() tells Django to manage our model through the admin site.

admin.site.register(Entry)