from django.core import serializers
from django.http import HttpResponse
from django.db.models import F, Q
from django.shortcuts import render

from results.models import StudentExam

def show(request):
    #q = StudentExam.objects.raw("select * from results")
    
    #q = StudentExam.objects.filter(score=F("planned")-10)

    q1 = Q(subject="Programming")
    q2 = Q(student="Max")
    q3 = Q(score__gt=F("planned"))

    # student is not Max and score > planned
    #q = StudentExam.objects.filter(~q2 & q3)

    # student is not Max and score > planned
    # OR subject is not programming
    #q = StudentExam.objects.filter((~q2 & q3) | ~q1)

    #s = "<br> ".join([str(item) for item in q])
    #return HttpResponse(s)

    # serialize queryset as xml
    #return HttpResponse(serializers.serialize("xml", q))

    #losers = StudentExam.objects.exclude(score__gte=F("planned"))
    #losers_of_second_semester = losers.filter(semester=2)
    #s = "<br> ".join([str(item) for item in losers_of_second_semester])
    #return HttpResponse(s)

    q = StudentExam.objects.filter(~q2)
    #return HttpResponse(q.values("student", "subject", "semester"))
    return HttpResponse(q.values_list("student", "subject", "semester"))

def info(request):

    q = StudentExam.objects.all()
    return render(request, "results/index.html", {"results" : q})