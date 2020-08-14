from django.contrib import admin
from .models import Post
from .models import Posty
from .models import Person

admin.site.register(Person)
admin.site.register(Post)
admin.site.register(Posty)

# Register your models here.
