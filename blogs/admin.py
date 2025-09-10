from django.contrib import admin
from .models import Category, Blogs, Comment

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  
    list_display=('name',)


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):  
    list_display=('title','category','author','is_published','pub_date')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'author', 'content', 'pub_date', 'is_approved')
    