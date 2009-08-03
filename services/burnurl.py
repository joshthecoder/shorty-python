## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url burnurl.com
class Burnurl(Service):

    def _test(self):
        # all we can test is shrink
        turl = self.shrink('http://test.com')
        if turl.startswith('http://burnurl.com'):
            return True
        else:
            return False

    def shrink(self, bigurl):
        resp = request('http://burnurl.com/', {'url': bigurl, 'output': 'plain'})
        return resp.read()

    def expand(self, tinyurl):
        # burnurl uses iframes for displaying original url
        # so we cannot expand them using the 301 redirect :(
        return None

