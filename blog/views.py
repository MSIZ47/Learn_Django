from django.shortcuts import render,get_object_or_404,redirect
from .models import Post, Category, Tags,Comments,Reply
from advertisment.models import AdvertisModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponseRedirect
from.forms import CommentsForm,ReplyForm,CreatPostForm
from django.contrib.auth.decorators import login_required




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




def blog_single(req,pid):
     if req.method =='GET':
          posts_id_list = []
          posts = Post.objects.filter(status = True )
          for post in posts:
               posts_id_list.append(post.id)
          posts_id_list.reverse()

          if posts_id_list.index(pid) == 0:
               next_post = posts.get(id = posts_id_list[1])
               previous_post = None
          elif posts_id_list.index(pid) == posts_id_list.index(posts_id_list[-1]):
               previous_post = posts.get(id =(posts_id_list[-2]))
               next_post = None
          else:
               next_post = posts.get(id = posts_id_list[posts_id_list.index(pid)+1])
               previous_post = posts.get(id = posts_id_list[posts_id_list.index(pid)-1])

          comments = Comments.objects.filter(which_post = pid)
          post = Post.objects.get(id=pid,status = True)
          replys = Reply.objects.all()
          post.counted_views+=1
          post.save()
          context = {
               'post':post,
               'next':next_post,
               'previous':previous_post,
               'comments':comments,
               'replys':replys,
               }
          return render(req,'blog/blog-single.html',context=context)
     

     elif req.method =='POST':
          form = CommentsForm(req.POST)
          if form.is_valid():
               form.save()
          return HttpResponseRedirect(req.path_info)


def reply(req,cid):
     if req.method == 'GET':
          comment = Comments.objects.get(id=cid)
          context = {
               'comment':comment
          }
          return render(req, 'blog/reply.html', context=context)
     
     elif req.method =='POST':
          form = ReplyForm(req.POST)
          if form.is_valid():
               form.save()
          return redirect('/blog')

def delete(req,cid):
     comment = Comments.objects.get(id=cid)
     comment.delete()
     return redirect('/blog')
     
def edit(req,cid):
     comment = Comments.objects.get(id=cid)
     if req.method=="GET":
          form_get = CommentsForm(instance=comment)
          context = {
               'form':form_get,
               'comment':comment
          }
          return render(req, 'blog/edit_comments.html',context=context)
     elif req.method=='POST':
          form_post = CommentsForm(req.POST,instance=comment)
          if form_post.is_valid():
               form_post.save()
          return redirect('/blog')
     
@login_required
def create_post(req):
     if req.method=="GET":
          form_get = CreatPostForm()
          context = {
               'form':form_get,
          }
          return render(req, 'blog/create_post.html',context=context)
     elif req.method=='POST':
          form_post = CreatPostForm(req.POST)
          if form_post.is_valid():
               form_post.save()
          return redirect('/blog')