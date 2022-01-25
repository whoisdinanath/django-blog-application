from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home , name='home'),
    path('blog/post/<str:pk>/', views.singlePost, name='single-post'),
    path('blog/category/', views.blogCategory, name='blog-category'),

    path('blog/add/', views.createBlog , name= 'create-blog'),
    path('blog/update/<str:pk>', views.updateBlog, name='update-blog'),
    path('blog/delete/<str:pk>', views.deleteBlog, name='delete-blog'),

    path('about/', views.aboutPage, name='about'),
    path('contact/', views.contact, name='contact'),

    path('blog/<str:pk>' ,views.categoryHome , name='home-category')

   
]