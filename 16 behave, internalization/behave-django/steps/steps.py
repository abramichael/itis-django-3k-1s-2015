from behave import *
from django.contrib.auth.models import User

@given(u'a new authorized user')
def step_impl(context):
    u = User.objects.create_user(username="user", password="pssw")
    context.client.login(username="user", password="pssw")

@then(u'he has access to {page}')
def step_impl(context, page):
    response = context.client.get(page)
    print page
    print response.status_code
    assert response.status_code == 200