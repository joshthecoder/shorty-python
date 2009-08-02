## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url is.gd
class Isgd(Service):

    def shrink(self, bigurl):
        resp = request('http://is.gd/api.php', {'longurl': bigurl})
        turl = resp.read()
        if turl.startswith('Error:'):
            raise ShortyError(turl)
        return turl

