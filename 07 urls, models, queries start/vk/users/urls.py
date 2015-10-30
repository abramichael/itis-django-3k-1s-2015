from django.conf.urls import include, url


urlpatterns = [
	url(r'(?P<user_id>\d+)?','users.views.show_user', name='show_user')

]