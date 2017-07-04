# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy import log, signals
from crawler.spiders.news import NewsSpider
from scrapy.utils.project import get_project_settings

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



class ScrapyCrawlSet(viewsets.ViewSet):
    """
    Request type: GET
    Start Scrapy News Crawler

    Headers:
    Language: en_US

    Response:

    """
    __name__ = 'ScrapyCrawl'

    def list(self, request):
        """
        Run Scrapy crawl
        :param request:
        :param format:
        :return:
        """

        spider = NewsSpider(domain='bbc.com')
        settings = get_project_settings()
        runner = CrawlerRunner(settings)
        runner.crawl(spider)
        if reactor.running is False:
            reactor.run(installSignalHandlers=0)

        return Response(status=status.HTTP_200_OK)
