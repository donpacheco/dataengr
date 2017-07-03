import os
import sys

sys.path.insert(1, os.getcwd())
from items import NewsItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from readability import Document


class NewsSpider(CrawlSpider):
	name = "news"
	allowed_domains = ["bbc.co.uk", "theguardian.com"]
	start_urls = [
	"http://www.bbc.co.uk/news/",
	"http://www.bbc.co.uk/news/technology/",
	"http://www.bbc.co.uk/news/sport/",
	"http://theguardian.com/international/",
	]

	rules = [Rule(LinkExtractor(allow=['\d+']), 'parse_story')]

	def parse_story(self, response):
		doc = Document(response.text)
		story = NewsItem()
		story['url'] = response.url
		story['headline'] = doc.short_title()
		story['body'] = doc.summary()
		yield story
