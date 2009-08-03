## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url hurl.ws
class Hurlws(Service):

    def __init__(self, username=None):
        self.username = username

    def shrink(self, bigurl):
        parameters = {'url': bigurl}
        if self.username:
            parameters['user'] = self.username
        resp = request('http://www.hurl.ws/api/', post_data=urlencode(parameters))
        return resp.read()

