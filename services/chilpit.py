## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url chilp.it
class Chilpit(Service):

    def shrink(self, bigurl):
        resp = request('http://chilp.it/api.php', {'url': bigurl})
        url = resp.read()
        if url.startswith('http://'):
            return url.strip()
        else:
            raise ShortyError(url)

    def expand(self, tinyurl):
        Service.expand(self, tinyurl)

        # needs fixing
        """turl = urlparse(tinyurl)
        if turl.netloc.lstrip('www.') != 'chilp.it':
            raise ShortyError('Not a chilp.it url')
        resp = request('http://p.chilp.it/api.php?' + turl.query)
        url = resp.read()
        if url.startswith('http://'):
            return url.strip('\n\r')
        else:
            raise ShortyError(url)"""

    # get click stats of the tinyurl
    def stats(self, tinyurl):
        turl = urlparse(tinyurl)
        if turl.netloc.lstrip('www.') != 'chilp.it':
            raise ShortyError('Not a chilp.it url')
        resp = request('http://s.chilp.it/api.php?' + turl.query)
        hit_count = resp.read()
        try:
            return int(hit_count)
        except:
            raise ShortyError('Url not found or invalid')

