from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    slug=models.SlugField(max_length=100, unique=True,blank=True,null=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Blogs(models.Model):
        title = models.CharField(max_length=200)
        slug=models.SlugField(max_length=100, unique=True,blank=True, null=True)
        content = models.TextField()
        image= models.ImageField(upload_to='blogs/')
        pub_date = models.DateTimeField(auto_now_add=True)
        author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
        category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
        is_published = models.BooleanField(default=True)

        def save(self, *args, **kwargs):
            if not self.slug:  # ✅ Generate slug from title if not set
                self.slug = slugify(self.title)
            super().save(*args, **kwargs)

        def __str__(self):
            return self.title
        

class Comment(models.Model):
    article = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
         return f"Comment by {self.author|default:'Anonymous'} on {self.blog}"