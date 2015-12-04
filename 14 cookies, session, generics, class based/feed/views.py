import time
from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from feed.models import Tweet
from feed.forms import TweetForm


@login_required(login_url="/login")
def index(request):
    tweets = Tweet.objects.order_by("-pub_date")
    return render(request, "feed/feed.html", {"tweets": tweets,
                                              "f": TweetForm()})


@login_required(login_url="/login")
def hello(request):
    return HttpResponse("HELLO!")


@login_required(login_url="/login")
def tweet(request):
    if request.method == "POST":
        # f = TweetForm(request.POST)
        # t = f.save(commit=False)
        # t.user = request.user
        # t.pub_date = datetime.now()
        # t.save()

        if "last_tweet" not in request.session:
            request.session["last_tweet"] = time.time()
        else:
            c = time.time() - request.session["last_tweet"]
            if c < 10:
                return HttpResponse("Not so fast, body, wait!")

        t = Tweet(user=request.user,
                      pub_date= datetime.now())
        f = TweetForm(request.POST, instance=t)
        f.save()

        # t = Tweet(user=request.user,
        #           txt=request.POST["txt"],
        #           pub_date=datetime.now()
        #           )
        # t.save()
    return HttpResponseRedirect(reverse("feed"))
