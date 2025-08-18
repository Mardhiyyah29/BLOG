
from django.shortcuts import render, get_object_or_404
from .models import Blogs, Category

# Create your views here.
def Home(request):
    stories = Blogs.objects.filter(is_published=True).order_by('-pub_date')
    categories = Category.objects.all()
    sport_news= Blogs.objects.filter(category__name="sport",is_published=True).order_by('-pub_date')[:5]
    banner_news = Blogs.objects.filter(is_published=True).order_by('-pub_date')[:1]
    # Fetching the latest 5 stories for each category
    politics_news = Blogs.objects.filter(category__name="politics", is_published=True).order_by
    ('-pub_date')[:5]
    slider_news = Blogs.objects.filter(is_published=True).order_by('-pub_date')[:8]
    carousel_news = Blogs.objects.filter(is_published=True).order_by('-pub_date')[:5]
    carousel_news2 = Blogs.objects.filter(is_published=True).order_by('-pub_date')[:3]
    politics_news2 = Blogs.objects.filter(is_published=True).order_by('-pub_date')[:5]


    return render(request,'home.html', {'stories': stories, 'categories': categories, 
                                        'sport_news':sport_news,'banner_news':banner_news, 'politics_news'
                                        :politics_news, 'slider_news':slider_news,'carousel_news':
                                        carousel_news,'carousel_news2':carousel_news2,
                                        'politics_news2':politics_news2})
                                        

def Category_article(request):
    return render(request, 'category_article.html')

def Blogs_details(request,id):
    blog=get_object_or_404(Blogs, id=id)
    Categories = Category.objects.all()
    return render(request, 'blogs_details.html', {'blog': blog, 'Categories': Categories})


