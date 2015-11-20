from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from feed.models import Tweet
from datetime import datetime

def index(request):
    tweets = Tweet.objects.all()
    
    return render(request, "feed/feed.html", {"tweets": tweets})


def tweet(request):
    if request.method=="POST":
        t = Tweet(user=User.objects.get(username='ma'),
                    txt = request.POST["txt"],
                    pub_date = datetime.now()
                    )
        t.save()
    return HttpResponseRedirect("/feed")