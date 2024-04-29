"""A python package that enhances speed and simplicity of parsing robots files."""

import requests
from .utils import _regex
from .utils import parser
from .utils.exceptions import *

__version__ = "0.1"
__description__ = "A python package that enhances speed and simplicity of parsing robots files."
__author__ = "xyzpw"
__license__ = "MIT"

def urlRobots(url: str, find_url: bool = False, **kwargs) -> dict:
    """Returns a website's robots file contents.

    :param url:      the url which points to the robots file
    :param find_url: attempts to find the default robots location

    :kwargs: additional arguments for `requests.get` function"""
    if find_url:
        url = getRobotsUrl(url)
    contents = requests.get(url, **kwargs).text
    return parser.getRobotsContents(contents)

def getRobotsUrl(link: str) -> str:
    """Returns the default robots location for a website.

    :param link: any uri of which will be replaced to the robots location"""
    url = _regex.searchForGroup(r"^(?P<url>https?://[a-z0-9\-\.]+?)(?<=[a-z0-9])(?:(?!\-\.)$|/.*?$)", link, "url")
    if url != None and "." in url:
        return "%s/robots.txt" % url

def getRobots(url: str, find_url: bool = True, **kwargs):
    """Creates an object which contains robots information.

    :param url:      the url of which will be used to parse the robots file contents
    :param find_url: attempts to find the default robots location

    :kwargs: additional parameters will be passed into the `get` function from the `requests` module"""
    if find_url:
        url = getRobotsUrl(url)
    pageContents = requests.get(url, **kwargs).text
    return parser.Robots(pageContents)
