# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from mongoengine import Document, EmbeddedDocument, fields

# Create your models here.


class NewsItem(Document):
    """
    News Items from Crawler
    """
    id = fields.ObjectIdField(required=False, db_field='_id')
    url = fields.URLField(required=True)
    headline = fields.StringField(required=False, null=True)
    body = fields.DynamicField(required=False, null=True)
