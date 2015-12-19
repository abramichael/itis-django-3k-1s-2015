from behave import *
from player import Player

@given(u'a new player')
def step_impl(context):
    context.p = Player()

@then(u'he should have name')
def step_impl(context):
    assert hasattr(context.p, "name")

@then(u'he should have hp')
def step_impl(context):
    assert hasattr(context.p, "hp")

@then(u'his hp should be {d}')
def step_impl(context, d):
    assert context.p.hp == int(d)

@given(u'two players')
def step_impl(context):
    context.p1 = Player()
    context.p2 = Player()

@when(u'first kicks second with power {d}')
def step_impl(context, d):
    context.oldHP = context.p2.hp
    context.p1.kick(context.p2, int(d))

@then(u'second\'s hp decrease on {d}')
def step_impl(context, d):
    assert context.oldHP - context.p2.hp == int(d)