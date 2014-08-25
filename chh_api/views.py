#coding:utf-8
__author__ = 'yc'

from django.http import HttpResponse, HttpResponseRedirect
from chh import models


def hello(request):
    return HttpResponse('hello world')

def news(request):
    return HttpResponse(models.getAllNews())