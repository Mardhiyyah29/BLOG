
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
                                        

def Category_article(request, slug):
    category=get_object_or_404(Category,slug=slug )
    articles = Blogs.objects.filter(category=category, is_published=True).order_by('-pub_date')
    categories = Category.objects.all()
    return render(request, 'category_article.html', {'category': category, 'articles': articles,
                                                       'categories': categories})

def Blogs_details(request,slug):
    blog=get_object_or_404(Blogs,slug=slug, is_published=True)
    Categories = Category.objects.all()
    return render(request, 'blogs_details.html', {'blog': blog, 'Categories': Categories})


def About(request):
    return render(request, 'about.html')

def Categories(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def Contact(request):
    return render(request, 'contact.html')

def Privacy(request):
    return render(request, 'privacy.html')

def Terms(request):
    return render(request, 'terms.html')