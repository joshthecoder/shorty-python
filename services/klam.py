## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url kl.am
class Klam(Service):

    def __init__(self, apikey=None):
        self.apikey = apikey

    def shrink(self, bigurl, tags=None):
        parameters = {'url': bigurl, 'format': 'text'}
        if self.apikey:
            parameters['api_key'] = self.apikey
        if tags:
            parameters['tags'] = tags
        resp = request('http://kl.am/api/shorten', parameters)
        return resp.read()

