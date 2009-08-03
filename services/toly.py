## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url to.ly
class Toly(Service):

    def shrink(self, bigurl):
        resp = request('http://to.ly/api.php', {'longurl': bigurl})
        return resp.read()

