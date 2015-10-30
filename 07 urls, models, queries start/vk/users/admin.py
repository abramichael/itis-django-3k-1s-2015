from django.contrib import admin

from users.models import RawUser
from msgs.models import Msg

admin.site.register(RawUser)
admin.site.register(Msg)
