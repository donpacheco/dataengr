# I'm sure that this is not good practice; I've come across using setuptools / setup.py to do a local dev install
# (e.g. http://stackoverflow.com/questions/1893598/pythonpath-vs-sys-path), but I just don't have the time to figure
# out the intricacies of that mechanism, so proper deployment will have to fall to the wayside for now.
import sys
import os
import unittest

sys.path.insert(1, os.getcwd())
from utils import fake_response, match_class


class UtilTest(unittest.TestCase):
    def test_match_class(self):
        result = match_class("class123")
        self.assertEqual(result, "*[contains(concat(' ', @class, ' '), ' class123 ')]")

    def test_fake_response(self):
        response = fake_response('tests/fixtures/example.html')
        self.assertEqual(200, response.status)
        self.assertEqual("http://www.bbc.co.uk", response.url)
        self.assertEqual([u"<div>Test</div>"], response.css('div').extract())

    if __name__ == '__main__':
        unittest.main()
