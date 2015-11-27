from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'feed.views.index', name="feed"),
    url(r'^tweet$', 'feed.views.tweet', name="tweet"),
    url(r'^hello$', 'feed.views.hello', name="hello"),
]