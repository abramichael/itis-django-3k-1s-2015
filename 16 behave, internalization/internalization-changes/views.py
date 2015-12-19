from datetime import datetime
import time
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from feed.models import Tweet
from feed.forms import TweetForm


@login_required(login_url="/login")
def index(request):
    tweets = Tweet.objects.order_by("-pub_date")
    return render(request, "feed/feed.html", {"tweets": tweets,
                                              "f": TweetForm()})


@login_required(login_url="/login")
def hello(request):
    hello_str = _("HELLO!")
    return HttpResponse(hello_str)


@login_required(login_url="/login")
def tweet(request):
    if request.method == "POST":
        # f = TweetForm(request.POST)
        # t = f.save(commit=False)
        # t.user = request.user
        # t.pub_date = datetime.now()
        # t.save()
        if "last_tweet_sec" in request.session:
            seconds = request.session["last_tweet_sec"]
            if time.time() - seconds < 10:
                wait_str = _("wait 10 secs, bro..")
                return HttpResponse(wait_str)

        t = Tweet(user=request.user,
                      pub_date= datetime.now())
        f = TweetForm(request.POST, instance=t)
        f.save()
        request.session["last_tweet_sec"] = time.time()

        # t = Tweet(user=request.user,
        #           txt=request.POST["txt"],
        #           pub_date=datetime.now()
        #           )
        # t.save()
    return HttpResponseRedirect(reverse("feed"))
