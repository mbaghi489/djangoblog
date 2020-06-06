from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import models
def article_list(request):
    articles=models.Article.objects.all().order_by('date')
    args={'articles':articles}
    return render(request,'articles/article_list.html',args)
