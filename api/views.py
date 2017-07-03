# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from serializers import NewsItemSerializer
from models import NewsItem


class NewsItemSet(MongoModelViewSet):
    """
    NewsItem REST Api built from DRF mongoengine

    Keyword Search api/news_item/?keyword="keyword"
    """

    lookup_field = 'id'
    serializer_class = NewsItemSerializer

    def get_queryset(self):
        queryset = NewsItem.objects.all()
        keyword = self.request.query_params.get('keyword', None)
        if keyword:
            return queryset.search_text(keyword)
        return queryset
