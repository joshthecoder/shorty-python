## Shorty
## Copyright 2009 Joshua Roesslein

## @url cli.gs
class Cligs(Service):

    def __init__(self, apikey=None, appid=None):
        self.apikey = apikey
        self.appid = appid

    def shrink(self, bigurl, title=None):
        parameters = {'url': bigurl}
        if title:
            parameters['title'] = title
        if self.apikey:
            parameters['key'] = self.apikey
        if self.appid:
            parameters['appid'] = self.appid
        resp = request('http://cli.gs/api/v1/cligs/create', parameters)
        return resp.read()

    def expand(self, tinyurl):
        # TODO: debug this some more, not working properly
        '''resp = request('http://cli.gs/api/v1/cligs/expand', {'clig': tinyurl})
        return resp.read()'''
        return get_redirect(tinyurl)

