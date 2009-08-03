## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url xr.com x.bb
class Xr(Service):

    def __init__(self, account_name=None):
        self.account_name = account_name

    def shrink(self, bigurl, custom=None, domain=None, direct=True):
        parameters = {'link': bigurl}
        if custom:
            parameters['custom'] = custom
        if domain:
            parameters['domain'] = domain
        if direct:
            parameters['direct'] = 'yes'
        if self.account_name:
            parameters['pid'] = self.account_name
        resp = request('http://api.xr.com/api', parameters)
        url = resp.read()
        if url.startswith('http'):
            return url
        else:
            raise ShortyError(url)

