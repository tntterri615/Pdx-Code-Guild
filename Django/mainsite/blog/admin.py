from django.contrib import admin

#from . import models
from .models import BlogPost, Comment

admin.site.register(BlogPost)
admin.site.register(Comment)
