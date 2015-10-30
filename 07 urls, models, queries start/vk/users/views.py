from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import render

from users.models import RawUser
from msgs.models import Msg

def show_user(request, user_id=None):
    # HARD CODE DON'T DO LIKE THAT!!!1111
    #probable_id = user_id if user_id else ""
    #return HttpResponse("I am on page: " + "/user/" + probable_id)

    #user_url = reverse("users:show_user", args=(user_id,))

    if user_id is None:

        #users = RawUser.objects.all()
        #users = RawUser.objects.order_by("-username")

        #users = RawUser.objects.filter(year__gte=1988)

        users = RawUser.objects.filter(username__contains="t", year__gt=1995)

        result = ", ".join([user.username for user in users])
        return HttpResponse(result)

    else:
        user = RawUser.objects.get(id=user_id)

        friends = user.friend.all()
        result = ", ".join([user.username for user in friends])
        return HttpResponse(result)




def show_user_messages(request, user_id):
    #u = RawUser.objects.get(id=user_id)
    #messages = Msg.objects.filter(recipient=u)

    #messages = Msg.objects.filter(sender_id=user_id)

    u = RawUser.objects.get(id=user_id)
    messages = u.msgs_received.all()

    result = ", ".join([m.text for m in messages])
    return HttpResponse(result)
