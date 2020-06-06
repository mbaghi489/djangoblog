from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    return HttpResponse("hello world")
