from django.shortcuts import render,redirect

#To view response on browser!
from django.http import HttpResponse

#REVERSE - AVOID HARDCODING THE URLS 
from django.urls import reverse

#Logging!
import logging

#importing Post model
from .models import Post

#initial req
# def index(request):
#     return HttpRe sponse("Hello world, You are at blog's index")
#VARIABLE INTERPOLATION
# def index(request):
#     blog_title = "Latest Posts"
#     return render(request,'blog/index.html',{'blog_title':blog_title})
#FOR TAG

#Make this var globally accessible by all views!
#static demo data
# posts = [
#         {'id':1,'title':'Post 1','content':'Content of Post 1'},
#         {'id':2,'title':'Post 2','content':'Content of Post 2'},
#         {'id':3,'title':'Post 3','content':'Content of Post 3'},
#         {'id':4,'title':'Post 4','content':'Content of Post 4'},
# ]

def index(request):
    blog_title = "Latest Posts"
    posts = Post.objects.all()
    return render(request,'blog/index.html',{'blog_title':blog_title,'posts':posts})


#DYNAMIC URLS
# def detail(request,post_id):
#     return HttpResponse(f"You are viewing post detail page. And ID is {post_id}")
def detail(request,post_id):
    #LOGGER IMPLEMENTATION
    # to fetch requested post's details!
    #returns {..} of matching post_id from url into "item" var, else returns None.
    
    #getting static data!
    # post = next((item for item in posts if item['id']== post_id),None)

    #getting data from model
    post = Post.objects.get(pk=post_id)

    #logging
    # logger = logging.getLogger("TESTING")
    # logger.debug(f'Post variable is {post}')

    #share the same!
    return render(request,'blog/detail.html',{'post':post})

#REDIRECTS, please do import redirect from shortcuts and reverse from urls!
def old_url_redirect(request):
    return redirect(reverse("blog:new_page_url"))

def new_url_view(request):
    return HttpResponse("This is the new URL")

