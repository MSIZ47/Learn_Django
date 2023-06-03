from django.urls import path
from .views import *



app_name='blog'

urlpatterns = [
    path('', blog_home , name='blog_home'),
    path('blog_single/<int:pid>', blog_single , name='blog_single'),
    path('tag/<str:tag>', blog_home , name='blog_home_with_tag'),
    path('author/<str:username>', blog_home , name='blog_home_with_user'),
    path('category/<str:cat>', blog_home , name='blog_home_with_cat'),
    path('search/', blog_home , name='blog_home_with_search'),
    path('reply/<int:cid>', reply , name='reply'),
    path('delete/<int:cid>', delete , name='delete'),
    path('edit/<int:cid>', edit , name='edit'),
    path('create_post/', create_post , name='create_post'),
]