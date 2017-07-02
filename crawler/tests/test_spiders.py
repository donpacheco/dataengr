import sys
import os
import logging

from unittest.case import TestCase

sys.path.insert(1, os.getcwd())
from crawler.spiders.news import NewsSpider
from crawler.utils import fake_response


logger = logging.getLogger()
logger.level = logging.INFO
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

class NewsSpiderTestCase(TestCase):
    """ Test module for NewsSpider """

    def setUp(self):
        self.spider = NewsSpider()

    def test_parse_story_bbc(self):
        response = fake_response('tests/fixtures/bbc.html', 'http://www.bbc.co.uk/sport/rugby-union/40469006')
        logging.getLogger().info(response)
        item = self.spider.parse_story(response)
        itemdict = dict(item.next())
        self.assertEqual(itemdict['url'],
            'http://www.bbc.co.uk/sport/rugby-union/40469006')
        self.assertEqual(itemdict['headline'],
            'British and Irish Lions: Warren Gatland warns of wounded All Blacks')

    def test_parse_story_guardian(self):
        response = fake_response('tests/fixtures/guardian.html', 'https://www.theguardian.com/travel/2017/jul/02/sailing-the-whitsundays-white-sand-snorkelling-and-a-blissful-digital-detox')
        logging.getLogger().info(response)
        item = self.spider.parse_story(response)
        itemdict = dict(item.next())
        self.assertEqual(itemdict['url'],
            'https://www.theguardian.com/travel/2017/jul/02/sailing-the-whitsundays-white-sand-snorkelling-and-a-blissful-digital-detox')
        self.assertEqual(itemdict['headline'],
            'Sailing the Whitsundays: white sand, snorkelling and a blissful digital detox')
