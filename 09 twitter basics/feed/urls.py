from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'feed.views.index', name="index"),
    url(r'^tweet$', 'feed.views.tweet', name="tweet"),
]