## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url short.to
class Shortto(Service):

    def shrink(self, bigurl):
        resp = request('http://short.to/s.txt', {'url': bigurl})
        return resp.read()

    def expand(self, tinyurl):
        resp = request('http://long.to/do.txt', {'url': tinyurl})
        url = resp.read()
        if url.startswith('http'):
            return url
        else:
            raise ShortyError(url)

