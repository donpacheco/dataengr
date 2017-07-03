# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mongoengine import Document, fields

# Create your models here.


class NewsItem(Document):
    """
    News Items from Crawler
    """
    id = fields.ObjectIdField(required=False, db_field='_id')
    url = fields.URLField(required=True)
    headline = fields.StringField(required=False, null=True)
    body = fields.DynamicField(required=False, null=True)

    meta = {'indexes': [
        {'fields': ['$headline', "$body"],
         'default_language': 'english',
         'weights': {'headline': 10, 'body': 2}
        }
    ]}
