## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url snipurl.com snipr.com sn.im snurl.com
class Snipurl(Service):

    def __init__(self, user=None, apikey=None):
        self.user = user
        self.apikey = apikey

    def _test(self):
        # prompt for username and apikey
        self.user = raw_input('snipurl username: ')
        self.apikey = raw_input('snipurl apikey: ')
        Service._test(self)

    def shrink(self, bigurl, custom=None, title=None, private_key=None,
                owner=None, include_private_key=False):
        if self.user is None or self.apikey is None:
            raise ShortyError('Must set an user and apikey')
        parameters = {
            'sniplink': bigurl,
            'snipuser': self.user,
            'snipapi': self.apikey,
            'snipformat': 'simple' 
        }
        if custom:
            parameters['snipnick'] = custom
        if title:
            parameters['sniptitle'] = title
        if private_key:
            parameters['snippk'] = private_key
        if owner:
            parameters['snipowner'] = owner
        if include_private_key:
            parameters['snipformat_includepk'] = 'Y'
        resp = request('http://snipurl.com/site/getsnip',
                        post_data=urlencode(parameters))
        return resp.read()

    def expand(self, tinyurl):
        # TODO: fetch detailed info
        url = Service.expand(self, tinyurl)
        if url.startswith('http'):
            return url
        else:
            raise ShortyError('Invalid url')

