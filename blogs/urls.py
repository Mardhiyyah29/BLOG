from django.urls import path,include
from . import views 
from .views import post_comment

urlpatterns = [
    path('', views.Home,name='home'),
    path('About', views.About,name='about'),
    path('Categories', views.Categories,name='categories'),
    path('Contact', views.Contact,name='contact'),
    path('privacy', views.Privacy,name='privacy'),
    path('terms', views.Terms,name='terms'),



    path('blog/<slug:slug>/', views.Blogs_details, name='blog'),
    path('category/<slug:slug>/', views.Category_article,name='category_article'),
    path('article/<slug:slug>/comment/', views.post_comment, name='post_comment'),  # New URL pattern for adding comments

    
]