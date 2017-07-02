# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from serializers import NewsItemSerializer
from models import NewsItem

# Create your views here.

class NewsItemSet(MongoModelViewSet):
    lookup_field = 'id'
    serializer_class = NewsItemSerializer

    def get_queryset(self):
        return NewsItem.objects.all()


def SearchKeyword():
    pass
