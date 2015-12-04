from django.conf.urls import url
from django.views.generic import list, TemplateView
from analytics.views import MyListView
from feed.models import Tweet

info = {
    #"model": Tweet,
    "template_name": "analytics/tweet_list.html",
    "queryset": Tweet.objects.filter(user__username__contains="na"),
}

urlpatterns = [
    url(r'^contacts$', TemplateView.as_view(template_name="analytics/contacts.html"), name="contacts"),
    #url(r'^tweets$', list.ListView.as_view(**info)),
    url(r'^tweets$', MyListView.as_view(**info)),
]