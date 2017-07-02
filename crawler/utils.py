import os
from scrapy.http import Request, TextResponse

def match_class(classname):
    """Return an xpath that matches class name"""
    return "*[contains(concat(' ', @class, ' '), ' " + classname + " ')]"


def fake_response(file_name=None, url=None):
    """Create a Scrapy fake HTTP response from a HTML file"""
    if not url:
        url = 'http://www.bbc.co.uk'

    request = Request(url=url)
    if file_name:
        if not file_name[0] == '/':
            responses_dir = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(responses_dir, file_name)
        else:
            file_path = file_name

        file_content = open(file_path, 'r').read()
    else:
        file_content = ''

    response = TextResponse(url=url, request=request, body=file_content,
                            encoding='utf-8')
    return response
