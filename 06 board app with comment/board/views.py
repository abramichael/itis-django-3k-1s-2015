from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from board.models import Post, Comment
import datetime

def index(request):
    posts = Post.objects.order_by("-published_at")
    #return HttpResponse("NYANYANYANYA!")
    return render(request, "index.html", {"posts": posts})

def post(request):
    p = Post(txt=request.POST["post"],
    		published_at=datetime.datetime.now()
    		)
    p.save()
    return HttpResponseRedirect("/")

def post_page(request, post_id):
    comments = Comment.objects.filter(post_id=post_id).order_by("-published_at")
    post = Post.objects.get(id=post_id)
    #return HttpResponse("NYANYANYANYA!")
    return render(request, "post.html", {"comments": comments, "post": post})

def comment(request, post_id):
    c = Comment(post_id=post_id,
    	txt=request.POST["comment_text"],
    	published_at=datetime.datetime.now()
    )
    c.save()
    return HttpResponseRedirect("/post/" + post_id)