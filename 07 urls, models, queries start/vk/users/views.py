from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render


def show_user(request, user_id=None):
    # HARD CODE DON'T DO LIKE THAT!!!1111
    #probable_id = user_id if user_id else ""
    #return HttpResponse("I am on page: " + "/user/" + probable_id)

    user_url = reverse("users:show_user", args=(user_id,))
    return HttpResponse("I am on page: " + user_url)
