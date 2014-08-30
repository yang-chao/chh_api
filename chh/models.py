#coding:utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
# * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
import json


def getAllNews(page, count):
    try:
        page = int(page)
        count = int(count)
    except ValueError:
        return -1

    if page <= 0:
        page = 1
    start = (page - 1) * count
    end = page * count
    all_news = News.objects.all()[start: end]
    data = []
    for news in all_news:
        d = dict()
        d['id'] = news.id
        d['title'] = news.title
        d['time'] = str(news.time.now())  # 时间转为字符串
        d['link'] = news.link
        d['author'] = news.author
        d['message_count'] = news.message_count
        d['category'] = news.category
        data.append(d)
    return json.dumps(data, ensure_ascii=False)


class News(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=45)
    link = models.CharField(max_length=100)
    time = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=45, blank=True)
    author = models.CharField(max_length=45, blank=True)
    message_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'

