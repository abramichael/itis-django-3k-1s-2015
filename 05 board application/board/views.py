from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from board.models import Post
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