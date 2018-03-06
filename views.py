from django.shortcuts import render, render_to_response
from django.template import Template, Context
# Create your views here.
from django.http import HttpResponse
from mysite import models

def hello(request):
    return HttpResponse("Hello world")


def insert(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        models.students.objects.create(username=username, password=password)
        models.students.save()
    return render_to_response('insert.html')

def list(request):
    people_list = models.students.objects.all()
    c = Context({"people_list": people_list})
    return render_to_response("showuser.html", c)