from unittest.case import TestCase

from scrapy.crawler import CrawlerRunner
from scrapy.http import Request
from scrapy.item import BaseItem
from scrapy.utils.spider import iterate_spider_output

import unittest


class TestSuite(unittest.TestCase):
    if __name__ == '__main__':
        suite = unittest.TestLoader().discover(".", pattern='test_*.py', top_level_dir=None)
        unittest.TextTestRunner(verbosity=2).run(suite)
