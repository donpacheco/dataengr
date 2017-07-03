# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import sys
import os
import logging

from bson.objectid import ObjectId
from rest_framework import status
from django.test import TestCase, Client
from django.core.urlresolvers import reverse, reverse_lazy

from ..models import NewsItem
from ..serializers import NewsItemSerializer

logger = logging.getLogger()
logger.level = logging.INFO
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

# initialize the APIClient app
client = Client()


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
        response = client.get('/api/news_item/', follow=True)
        # get data from db
        news = NewsItem.objects.all()
        serializer = NewsItemSerializer(news, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleNewsTest(TestCase):
    """ Test module for GET single News API """

    def setUp(self):
        NewsItem.objects.all().delete()
        self.heady = NewsItem.objects.create(
            url='http://bbc.com/news/abc',
            headline='Heady Headline', body='<html>')
        self.sports = NewsItem.objects.create(
            url='http://bbc.com/sports/1234',
            headline='Sports Headline', body='<html>')
        self.guardian = NewsItem.objects.create(
            url='http://guardian.com/news/abc',
            headline='Guardian Headline', body='<html>')
        self.uksports = NewsItem.objects.create(
            url='http://bbc.co.uk/sports/1234',
            headline='UK Sports Headline', body='<html>')

    def test_get_valid_single_news(self):
        response = client.get("/api/news_item/"+str(self.sports.pk), follow=True)
        news = NewsItem.objects.get(id=self.sports.pk)
        serializer = NewsItemSerializer(news)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_news(self):
        response = client.get("/api/news_item/"+
            str(ObjectId("5958353d72d781adf5fd1a6d")), follow=True)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewNewsTest(TestCase):
    """ Test module for inserting a new news """

    def setUp(self):
        self.valid_payload = {
            'url': 'http://bbc.co.uk/technology/3422352',
            'headline': 'Massive Tech Attack',
            'body': '<html></html>'
        }

        self.invalid_payload = {
            'url': '',
            'headline': 'Sports Center',
            'body': '<html>'
        }

    def test_create_valid_news(self):
        response = client.post("/api/news_item/",
            data=json.dumps(self.valid_payload),
            content_type='application/json', follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_news(self):
        response = client.post("/api/news_item/",
            data=json.dumps(self.invalid_payload),
            content_type='application/json', follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleNewsTest(TestCase):
    """ Test module for updating an existing news record """

    def setUp(self):
        NewsItem.objects.all().delete()
        self.heady = NewsItem.objects.create(
            url='http://bbc.com/news/abc',
            headline='Heady Headline', body='<html>')
        self.sports = NewsItem.objects.create(
            url='http://bbc.com/sports/1234',
            headline='Sports Headline', body='<html>')
        self.guardian = NewsItem.objects.create(
            url='http://guardian.com/news/abc',
            headline='Guardian Headline', body='<html>')
        self.uksports = NewsItem.objects.create(
            url='http://bbc.co.uk/sports/1234',
            headline='UK Sports Headline', body='<html>')
        self.valid_payload = {
            'url': 'http://bbc.co.uk/technology/3422352',
            'headline': 'Massive Tech Attack',
            'body': '<html></html>'
        }

        self.invalid_payloader = {
            'url': "1",
            'headline': 'Sports Center',
            'body': '<html>'
        }

    def test_valid_update_news(self):
        response = client.put("/api/news_item/"+str(self.guardian.pk),
            data=json.dumps(self.valid_payload),
            content_type='application/json', follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_news(self):
        response = client.put("/api/news_item/",
            data=json.dumps(self.invalid_payloader),
            content_type='application/json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)


class DeleteSingleNewsTest(TestCase):
    """ Test module for deleting an existing news record """

    def setUp(self):
        NewsItem.objects.all().delete()
        self.heady = NewsItem.objects.create(
            url='http://bbc.com/news/abc',
            headline='Heady Headline', body='<html>')
        self.sports = NewsItem.objects.create(
            url='http://bbc.com/sports/1234',
            headline='Sports Headline', body='<html>')
        self.guardian = NewsItem.objects.create(
            url='http://guardian.com/news/abc',
            headline='Guardian Headline', body='<html>')
        self.uksports = NewsItem.objects.create(
            url='http://bbc.co.uk/sports/1234',
            headline='UK Sports Headline', body='<html>')

    def test_valid_delete_news(self):
        response = client.delete("/api/news_item/"+str(self.guardian.pk), follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_delete_news(self):
        response = client.delete("/api/news_item/"+
            str(ObjectId("5958353d72d781adf5fd1a6d")), follow=True)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
