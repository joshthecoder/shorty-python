## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

# tinyurl.com
class Tinyurl(Service):

    def shrink(self, bigurl):
        resp = request('http://tinyurl.com/api-create.php', {'url': bigurl})
        return resp.read()

