from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from feed.models import Tweet


class MyListView(ListView):

    queryset = Tweet.objects.all()
    template_name = "analytics/tweet_list.html"

    def get_context_data(self, **kwargs):
        users = User.objects.all()
        context = super(MyListView, self).get_context_data(**kwargs)
        context["users"] = users
        return context

