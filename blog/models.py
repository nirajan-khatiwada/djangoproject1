from django.db import models
from django.utils.text import slugify
# Create your models here
class Author(models.Model):
    Fname=models.CharField(max_length=50)
    Lname=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    def __str__(self):
        return f'{self.Fname}{self.Lname}'


class Tag(models.Model):
    Caption=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.Caption}'


class Post(models.Model):
    title=models.CharField(max_length=50)
    excerpt=models.CharField(max_length=250,null=True)
    date=models.DateTimeField(auto_now_add=True,editable=False)
    slug=models.SlugField(primary_key=True,db_index=True,blank=True)
    content=models.TextField(null=True,blank=True)
    author=models.ForeignKey(Author,on_delete=models.SET_DEFAULT,related_name="author_query",default="No Author",db_constraint=False)
    caption=models.ManyToManyField(Tag,related_name="lol")
    image=models.ImageField(upload_to="image",max_length=200,null=True)
    def __str__(self):
        return f'{self.title}'
    def save(self,*args,**kwargs):
        if(not(self.slug)):
            self.slug=slugify(self.title)
        super().save(*args,**kwargs)


