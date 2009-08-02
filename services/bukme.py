## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url buk.me
class Bukme(Service):

    def _process(self, resp):
        # bukme returns some markup after the url, so chop it off
        url = resp[:resp.find('<')]
        if url.startswith('http://'):
            return url
        else:
            raise ShortyError(url)

    def shrink(self, bigurl, tag=None):
        parameters = {'url': bigurl}
        if tag:
            parameters['buk'] = tag
        resp = request('http://buk.me/api.php', parameters)
        return self._process(resp.read())

    def expand(self, tinyurl):
        resp = request('http://buk.me/api.php', {'rev': tinyurl})
        return self._process(resp.read())

