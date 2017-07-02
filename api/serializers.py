from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers

from models import NewsItem


class NewsItemSerializer(mongoserializers.DocumentSerializer):
    class Meta:
        model = NewsItem
        exclude = ['auto_id_0']
        depth = 1
