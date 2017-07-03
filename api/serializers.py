from rest_framework_mongoengine import serializers

from models import NewsItem


class NewsItemSerializer(serializers.DocumentSerializer):
    class Meta:
        model = NewsItem
        exclude = ['auto_id_0']
        depth = 1
