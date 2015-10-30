from django.conf.urls import include, url


urlpatterns = [
	url(r'^(?P<user_id>\d+)?/$','users.views.show_user', name='show_user'),
    url(r'(?P<user_id>\d+)/messages','users.views.show_user_messages', 
        name='show_user_messages'),
]