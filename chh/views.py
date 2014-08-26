#coding:utf-8
# Create your views here.
from django.http import HttpResponse, Http404
from chh import models


def news(request, page, count):
    result = models.getAllNews(page, count)
    if request == -1:
        raise Http404()
    else:
        return HttpResponse(result)

