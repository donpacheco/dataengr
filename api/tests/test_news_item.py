# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from rest_framework import status
from django.test import TestCase, Client

from ..models import NewsItem
from ..serializers import NewsItemSerializer

# initialize the APIClient app
client = Client()

class NewsItemTest(TestCase):
    """ Test module for NewsItem model """

    def setUp(self):
        NewsItem.objects.all().delete()
        NewsItem.objects.create(
            url='http://bbc.com/news/abc', headline='Heady Headline', body='<html>')
        NewsItem.objects.create(
            url='http://bbc.com/sports/1234', headline='Sports Headline', body='<html>')

    def test_news_item(self):
        news_headliner = NewsItem.objects.get(url='http://bbc.com/news/abc')
        news_sports = NewsItem.objects.get(url='http://bbc.com/sports/1234')
        self.assertEqual(
            news_headliner.headline, "Heady Headline")
        self.assertEqual(
            news_sports.headline, "Sports Headline")

class GetAllNewsItemTest(TestCase):
    """ Test module for GET all NewsItem API """

    def setUp(self):
        NewsItem.objects.all().delete()
        NewsItem.objects.create(
            url='http://bbc.com/news/abc', headline='Heady Headline', body='<html>')
        NewsItem.objects.create(
            url='http://bbc.com/sports/1234', headline='Sports Headline', body='<html>')
        NewsItem.objects.create(
            url='http://guardian.com/news/abc', headline='Guardian Headline', body='<html>')
        NewsItem.objects.create(
            url='http://bbc.co.uk/sports/1234', headline='UK Sports Headline', body='<html>')

    def test_get_all_news(self):
        # get API response
        response = client.get('/api/news_item/')
        # get data from db
        news = NewsItem.objects.all()
        serializer = NewsItemSerializer(news, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
