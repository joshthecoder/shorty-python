## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## Common code used in all compiled versions of shorty.

class ShortyError(Exception):

    def __init__(self, reason):
        self.reason = str(reason)

    def __str__(self):
        return repr(self.reason)

"""Do a http request"""
def request(url, parameters=None, username_pass=None, post_data=None):

    # build url + parameters
    if parameters:
        url_params = '%s?%s' % (url, urlencode(parameters))
    else:
        url_params = url

    # if username and pass supplied, build basic auth header
    headers = {}
    if username_pass:
        headers['Authorization'] = 'Basic %s' % base64.b64encode('%s:%s' % username_pass)

    # send request
    try:
        req = Request(url_params, headers=headers)
        if post_data:
            req.add_data(post_data)
        return urlopen(req)
    except URLError, e:
        raise ShortyError(e)

def get_redirect(url):

    class StopRedirectHandler(HTTPRedirectHandler):
        def http_error_301(self, req, fp, code, smg, headers):
            return None
        def http_error_302(self, req, fp, code, smg, headers):
            return None
    o = build_opener(StopRedirectHandler())
    try:
        o.open(url)
    except HTTPError, e:
        if e.code == 301 or e.code == 302:
            return e.headers['Location']
        else:
            raise ShortyError(e)
    except URLError, e:
        raise ShortyError(e)
    return None

"""Base interface that all services implement."""
class Service(object):

    tested = False

    def _test(self):
        self.tested = True

        # first shrink an url
        try:
            turl = self.shrink('http://test.com')
        except ShortyError, e:
            raise ShortyError('@shrink ' + e.reason)

        # second expand url and verify
        try:
            if self.expand(turl) == 'http://test.com':
                return True
            elif self.expand(turl) == 'http://test.com/':
                return True
            else:
                return False
        except ShortyError, e:
            raise ShortyError('@expand ' + e.reason)

    def shrink(self, bigurl):
        """Take a big url and make it smaller"""
        return None

    def expand(self, tinyurl):
        """Take a tiny url and make it bigger"""
        return get_redirect(tinyurl)

"""
Shrink the given url for the specified service domain.
Returns the tiny url OR None if service not supported.
"""
def shrink(service_domain, bigurl, *args, **kargs):

    s = services.get(service_domain)
    if not s:
        return None
    return s.shrink(bigurl, *args, **kargs)
    
"""
Expand tiny url into its full url.
Returns long url if successful or None if failure.
"""
def expand(tinyurl):

    turl = urlparse(tinyurl)
    domain = turl.netloc.lower()
    if domain.startswith('www.'):
        # strip off www. if present
        domain = domain[4:]
    s = services.get(domain)
    if not s:
        return get_redirect(tinyurl)
    return s.expand(tinyurl)
