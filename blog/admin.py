from django.contrib import admin
from django.contrib.auth.models import User
from .models import Post, Experience, Education, Interest

admin.site.register(Post)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Interest)


# Register your models here.
