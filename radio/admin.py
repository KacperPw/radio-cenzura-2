from django.contrib import admin
from .models import Category, Subcategory, Post, PostIndex, Event


# Register your models here.
from django.contrib import admin
from .models import Category, Subcategory, Post

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Post)
admin.site.register(PostIndex)
admin.site.register(Event)