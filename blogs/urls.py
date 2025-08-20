from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.Home,name='home'),
    path('About', views.About,name='about'),
    path('Categories', views.Categories,name='categories'),
    path('Contact', views.Contact,name='contact'),
    path('privacy', views.Privacy,name='privacy'),
    path('terms', views.Terms,name='terms'),



    path('Blog/<slug:slug>/', views.Blogs_details, name='blog'),
    path('Category/<slug:slug>/', views.Category_article,name='category_article'),
    
]