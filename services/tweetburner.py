## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url tweetburner.com twurl.nl
class Tweetburner(Service):

    def shrink(self, bigurl):
        resp = request('http://tweetburner.com/links', post_data='link[url]=%s' % bigurl)
        return resp.read()

