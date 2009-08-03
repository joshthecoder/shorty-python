## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url digg.com
class Digg(Service):

    def __init__(self, appkey=None):
        self.appkey = appkey
        self.itemid = None
        self.view_count = None

    def _test(self):
        self.appkey = 'http://gitorious.org/shorty'
        Service._test(self)

    def shrink(self, bigurl):
        # FIXME: python 2.4 runs into a 403 error for some reason
        if not self.appkey:
            raise ShortyError('Must set an appkey')
        resp = request('http://services.digg.com/url/short/create',
            {'url': bigurl, 'appkey': self.appkey, 'type': 'json'})
        jdata = json.loads(resp.read())['shorturls'][0]
        self.itemid = jdata['itemid']
        self.view_count = jdata['view_count']
        return str(jdata['short_url'])

    def expand(self, tinyurl):
        if self.appkey:
            turl = urlparse(tinyurl)
            if turl[1].lstrip('www.') != 'digg.com':
                raise ShortyError('Not a valid digg url')
            resp = request('http://services.digg.com/url/short/%s' % quote(
                            turl[2].strip('/')),
                            {'appkey': self.appkey, 'type': 'json'})
            jdata = json.loads(resp.read())['shorturls'][0]
            self.itemid = jdata['itemid']
            self.view_count = jdata['view_count']
            return str(jdata['link'])
        else:
            self.itemid = None
            self.view_count = None
            return get_redirect(tinyurl)

