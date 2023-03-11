from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategoria"

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Subkategorie"
        verbose_name_plural = "Subkategoria"

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    audio_file = models.FileField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Posty w Kategoriach"
        verbose_name_plural = "Post w Kategorii"

    def __str__(self):
        return self.title

class PostIndex(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    post_index_img = models.ImageField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', null=True)
    updated_on = models.DateTimeField(auto_now= True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        verbose_name = "Posy na Stronie Głównej"
        verbose_name_plural = "Post na Stronie Głównej"


    def __str__(self):
        return self.title
    
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    event_date = models.DateField()
    time = models.TimeField(null=True)
    ticket_url = models.URLField(blank=True, null=True)
    link_urkl = models.URLField(blank=True, null=True)
    ticket_status = models.BooleanField(null=True)
    link_status = models.BooleanField(null=True)
    
    class Meta:
        verbose_name = "Wydarzenie"
        verbose_name_plural = "Wydarzenia"
    
    def __str__(self):
        return self.title
    
