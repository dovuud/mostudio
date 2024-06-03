from django.shortcuts import render,get_object_or_404
from .models import *



# Create your views here.

def home_view(request):
    posts = Post.objects.all().order_by('-id')[:5]
    category = Category.objects.all()
    context = {'posts':posts, 'category':category}
    return render(request, 'index.html', context)

def about_view(request):
    about = About.objects.all().order_by('-id')[:1]
    context = {'about':about}
    return render(request,'about.html',context)

def contact_view(request):
    contact = Contact.objects.all().order_by('-id')[:1]
    context = {'contact':contact}
    return render(request,'contact.html',context)

def blog_view(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts':posts}
    return render(request,'blog.html', context)

