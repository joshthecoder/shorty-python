## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url budurl.com
class Budurl(Service):

    def __init__(self, apikey=None):
        self.apikey = apikey

    def _test(self):
        #prompt for apikey
        self.apikey = raw_input('budurl apikey: ')
        Service._test(self)

    def shrink(self, bigurl, notes=None):
        if self.apikey is None:
            raise ShortyError('Must set an apikey')
        parameters = {'long_url': bigurl, 'api_key': self.apikey}
        if notes:
            parameters['notes'] = notes
        resp = request('http://budurl.com/api/v1/budurls/shrink', parameters)
        jdata = json.loads(resp.read())
        if jdata['success'] != 1:
            raise ShortyError(jdata['error_message'])
        else:
            return str(jdata['budurl'])

    def expand(self, tinyurl):
        resp = request('http://budurl.com/api/v1/budurls/expand', {'budurl': tinyurl})
        jdata = json.loads(resp.read())
        if jdata['success'] != 1:
            raise ShortyError(jdata['error_message'])
        else:
            return str(jdata['long_url'])

