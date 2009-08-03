## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url tr.im
class Trim(Service):

    def __init__(self, apikey=None, username_pass=None):
        self.apikey = apikey
        self.username_pass = username_pass

    def shrink(self, bigurl, custom=None, searchtags=None, privacycode=None,
                newtrim=False, sandbox=False):
        parameters = {}
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
        if self.apikey:
            parameters['api_key'] = self.apikey
        resp = request('http://api.tr.im/api/trim_url.json', parameters, self.username_pass)
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
        if turl[1].lstrip('www.') != 'tr.im':
            raise ShortyError('Not a valid tr.im url')
        parameters = {'trimpath': turl[2].strip('/')}
        if self.apikey:
            parameters['api_key'] = self.apikey
        resp = request('http://api.tr.im/api/trim_destination.json', parameters)
        jdata = json.loads(resp.read())
        self.status = (int(jdata['status']['code']), str(jdata['status']['message']))
        if not 200 <= self.status[0] < 300:
            raise ShortyError(self.status[1])
        return str(jdata['destination'])

