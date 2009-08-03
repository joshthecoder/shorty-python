## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url hex.io
class Hexio(Service):

    def shrink(self, bigurl):
        resp = request('http://hex.io/api-create.php', {'url': bigurl})
        url = resp.read()
        if url.startswith('http'):
            return url
        else:
            raise ShortyError('Failed to shrink url')

