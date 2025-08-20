from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    slug=models.SlugField(max_length=100, unique=True,blank=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Blogs(models.Model):
        title = models.CharField(max_length=200)
        slug=models.SlugField(max_length=100, unique=True,blank=True,)
        content = models.TextField()
        image= models.ImageField(upload_to='blogs/')
        pub_date = models.DateTimeField(auto_now_add=True)
        author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
        category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
        is_published = models.BooleanField(default=True)
        def __str__(self):
            return self.title
        

