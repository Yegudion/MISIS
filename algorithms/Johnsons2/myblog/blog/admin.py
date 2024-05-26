# blog/admin.py
from django.contrib import admin
# from .models import Post, Engineer
from .models import Engineer, Task


# admin.site.register(Post)
admin.site.register(Engineer)
admin.site.register(Task)
