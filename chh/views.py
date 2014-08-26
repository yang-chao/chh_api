#coding:utf-8
# Create your views here.
from django.http import HttpResponse
from chh import models


def news(request):
    return HttpResponse(models.getAllNews())