from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Blog, Category, About
from .forms import BlogCreation, CommentForm , ContactForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
   

# Create your views here.
def home(request):
    query = ''
    if request.GET.get('query'):
        query = request.GET.get('query')
    categories = Category.objects.filter(name__icontains=query)
    posts = Blog.objects.distinct().filter(Q(title__icontains=query) | Q(overview__icontains=query) | Q(category__in=categories))
    
    
    page = request.GET.get('page')
    results = 2
    paginator = Paginator(posts, results)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        page=1
        posts = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        posts = paginator.page(page)

    leftIndex = (int(page)  - 1 )
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page)+ 2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages+1

    custom_index = range(leftIndex, rightIndex)
    
    
    context={
        'posts':posts, 'query':query, 'custom_index':custom_index
    }
    
    return render(request, 'posts/home.html', context)


def categoryHome(request, pk):
    query = ''
    if request.GET.get('query'):
        query = request.GET.get('query')
    posts = Blog.objects.filter(category__id=pk)
    posts = posts.distinct().filter(Q(title__icontains=query) | Q(overview__icontains=query))
    
    
    page = request.GET.get('page')
    results = 2
    paginator = Paginator(posts, results)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        page=1
        posts = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        posts = paginator.page(page)

    leftIndex = (int(page)  - 1  )
    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page)+ 2)
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages+1

    custom_index = range(leftIndex, rightIndex)
    
    
    context={
        'posts':posts, 'query':query, 'custom_index':custom_index
    }
    
    return render(request, 'posts/home.html', context)


def singlePost(request, pk):
    post = Blog.objects.get(id=pk)
    categories = Category.objects.all()
    related_post = post.category.blog_set.all().exclude(id=pk)

    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.blog = post
        comment.save()

        post.getCommentCount

        messages.success(request, 'Comment submitted succesfully!')
        return redirect('single-post', pk=post.id)

    context = {
        'post':post, 'categories':categories, 'related':related_post, 'form':form
    }
    return render(request, 'posts/post.html', context)


def blogCategory(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'posts/blog-category.html', context)

@login_required()
def createBlog(request):
    author = request.user
    form = BlogCreation()
    if request.method == "POST":
        form = BlogCreation(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = author
            blog.save()
            messages.success(request, 'Blog post added succesfully!')
            return redirect('home')


    context = {
        'form':form
    }
    return render(request, 'posts/blog_form.html', context)


@login_required()
def updateBlog(request, pk):
    author = request.user
    post = author.blog_set.get(id=pk)
    form = BlogCreation(instance=post)
    if request.method == 'POST':
        form = BlogCreation(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post updated succesfully!')
            return redirect('home')


    context = {
        'form':form , 'post':post

    }
    return render(request, 'posts/blog_form.html', context)


@login_required()
def deleteBlog(request, pk):
    author = request.user
    post = author.blog_set.get(id=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Blog post deleted succesfully!')
        return redirect('home')
    context = {
'object':post
    }
    return render(request, 'delete_template.html', context)


def aboutPage(request):
    about = About.objects.first()
    context = {
'about':about
    }
    return render(request, 'posts/about.html', context)


def contact(request):
    about = About.objects.first()
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            messages.success(request, 'Message sent succesfully!')
            return redirect('contact')
    context = {
'form':form, 'about':about
    }
    return render(request, 'posts/contact.html', context)