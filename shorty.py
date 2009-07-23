"""
     _                _
 ___| |__   ___  _ __| |_ _   _ 
/ __| '_ \ / _ \| '__| __| | | |
\__ \ | | | (_) | |  | |_| |_| |
|___/_| |_|\___/|_|   \__|\__, |
                           __/ |
                          |___/ 

Access many URL shortening services from one library.

Python 2.4+
Versions before 2.6 require simplejson.

http://gitorious.org/shorty

MIT License
Copyright (c) 2009 Joshua Roesslein <jroesslein at gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from urllib2 import urlopen, URLError, HTTPError
from urllib import urlencode
from urlparse import urlparse
import base64

try:
    import json
except:
    import simplejson as json

class ShortyError(Exception):

    def __init__(self, reason):
        self.reason = str(reason)

    def __str__(self):
        return repr(self.reason)

"""Wrap urlopen to raise shorty errors instead"""
def request(*args, **kargs):

    try:
        return urlopen(*args, **kargs)
    except URLError, e:
        raise ShortyError(e)

"""Build basic auth header value"""
def basic_auth(username, password):

    return 'Basic %s' % base64.b64encode('%s:%s' % (username, password))

"""Base interface that all services implement."""
class Service(object):

    def shrink(bigurl):
        """Take a big url and make it smaller"""

        return None

    def expand(tinyurl):
        return None

"""Tinyurl.com"""
class Tinyurl(Service):

    @staticmethod
    def shrink(bigurl):
        resp = request('http://tinyurl.com/api-create.php?url=%s' % bigurl)
        return resp.readline()

"""Tr.im"""
class _Trim(Service):

    def __init__(self, apikey=None, username=None, password=None):
        self.base_param = {}
        if apikey:
            self.base_param['api_key'] = apikey
        if username and password:
            self.base_param['Authorization'] = basic_auth(username, password)

    def shrink(self, bigurl, custom=None, searchtags=None, privacycode=None,
                newtrim=False, sandbox=False):
        parameters = {}
        parameters.update(self.base_param)
        parameters['url'] = bigurl
        if custom:
            parameters['custom'] = custom
        if searchtags:
            parameters['searchtags'] = searchtags
        if privacycode:
            parameters['privacycode'] = privacycode
        if newtrim:
            parameters['newtrim'] = '1'
        if sandbox:
            parameters['sandbox'] = '1'
        url = 'http://api.tr.im/api/trim_url.json?%s' % urlencode(parameters)
        resp = request(url)
        jdata = json.loads(resp.read())
        self.status = (int(jdata['status']['code']), str(jdata['status']['message']))
        if not 200 <= self.status[0] < 300:
            raise ShortyError(self.status[1])
        self.trimpath = str(jdata['trimpath'])
        self.reference = str(jdata['reference'])
        self.destination = str(jdata['destination'])
        self.domain = str(jdata['domain'])
        return str(jdata['url'])

    def expand(self, tinyurl):
        turl = urlparse(tinyurl)
        if turl.netloc != 'tr.im' and turl.netloc != 'www.tr.im':
            raise ShortyError('Not a valid tr.im url')
        parameters = {}
        parameters.update(self.base_param)
        parameters['trimpath'] = turl.path.strip('/')
        url = 'http://api.tr.im/api/trim_destination.json?%s' % urlencode(parameters)
        resp = request(url)
        jdata = json.loads(resp.read())
        self.status = (int(jdata['status']['code']), str(jdata['status']['message']))
        if not 200 <= self.status[0] < 300:
            raise ShortyError(self.status[1])
        return str(jdata['destination'])

Trim = _Trim()  # non-authenticated, no apikey instance
        
