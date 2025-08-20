from django.contrib import admin
from .models import Category, Blogs

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):  
    list_display=('name',)


@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):  
    list_display=('title','category','author','is_published','pub_date')
