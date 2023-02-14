from django.contrib import admin
from .models import Post

# Granting access to the table of Posts to the administrator
admin.site.register(Post)
