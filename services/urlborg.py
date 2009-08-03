## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url urlborg.com ub0.cc
class Urlborg(Service):

    def __init__(self, apikey=None):
        self.apikey = apikey

    def _test(self):
        # prompt tester for apikey
        self.apikey = raw_input('urlborg apikey: ').strip()
        Service._test(self)

    def shrink(self, bigurl):
        if not self.apikey:
            raise ShortyError('Must set an apikey')
        url = 'http://urlborg.com/api/%s/create/%s' % (self.apikey, quote(bigurl))
        resp = request(url)
        turl = resp.read()
        if not turl.startswith('http://'):
            raise ShortyError(turl)
        return turl

    def expand(self, tinyurl):
        if not self.apikey:
            return get_redirect(get_redirect(tinyurl))
        turl = urlparse(tinyurl)
        url = 'http://urlborg.com/api/%s/url/info.json%s' % (self.apikey, turl[2])
        resp = request(url)
        jdata = json.loads(resp.read())
        if jdata.has_key('error'):
            raise ShortyError('Invalid tiny url or apikey')
        return str(jdata['o_url'])

