from django.shortcuts import render
from .models import Post, Category, Tags
from advertisment.models import AdvertisModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.



def blog_home(req, tag=None, username=None, cat=None):
    posts = Post.objects.filter(status=True)
    category = Category.objects.all()
    tags = Tags.objects.all()
    last_four_posts = posts[:4]
    adv = AdvertisModel.objects.all()[3]

    if tag:
         posts = Post.objects.filter(tag__name=tag)


    if username:
         posts = Post.objects.filter(author__username=username)
        
    if cat:
         posts = Post.objects.filter(category__name=cat)

    if req.GET.get('search'):
         posts = Post.objects.filter(content__contains=req.GET.get('search'))

    posts = Paginator(posts, 2)

    try:
         page_number = req.GET.get('page')
         posts = posts.get_page(page_number)


    except PageNotAnInteger:
         posts = posts.get_page(1)
     
    except EmptyPage:
         posts = posts.get_page(1)
         
    context = {
        'posts' : posts,
        'category' : category,
        'last_four_posts' : last_four_posts,
        'tags' : tags,
        'ADV' : adv,
    }
    return render(req, 'blog/blog-home.html', context=context)