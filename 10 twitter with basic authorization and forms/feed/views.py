from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from feed.models import Tweet
from datetime import datetime
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login")
def index(request):
    tweets = Tweet.objects.all()
    
    return render(request, "feed/feed.html", {"tweets": tweets})

@login_required(login_url="/login")
def hello(request):
    return HttpResponse("HELLO!")

@login_required(login_url="/login")
def tweet(request):
    if request.method=="POST":
        t = Tweet(user=request.user,
                    txt = request.POST["txt"],
                    pub_date = datetime.now()
                    )
        t.save()
    return HttpResponseRedirect(reverse("feed"))