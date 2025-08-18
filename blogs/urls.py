from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.Home,name='home'),
    path('Blog/<int:id>/', views.Blogs_details, name='blog'),
    path('Category/', views.Category_article,name='category_article'),
    
]