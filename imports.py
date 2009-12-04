## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## Do all importing here
from urllib2 import urlopen, Request, URLError, HTTPError, HTTPRedirectHandler, build_opener
from urllib import urlencode, quote
from urlparse import urlparse
from random import randint
import base64
from getpass import getpass
import re

try:
    import json
except:
    import simplejson as json
