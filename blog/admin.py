from django.contrib import admin

# Register your models here.

from .models import Entry, Comment

admin.site.register(Entry)
admin.site.register(Comment)