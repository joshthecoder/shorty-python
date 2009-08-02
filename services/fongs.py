## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url fon.gs
class Fongs(Service):

    def shrink(self, bigurl, tag=None):
        parameters = {'url': bigurl}
        if tag:
            parameters['linkname'] = tag
        resp = request('http://fon.gs/create.php', parameters)
        data = resp.read()
        if data.startswith('OK:'):
            return data.lstrip('OK: ')
        elif data.startswith('MODIFIED:'):
            return data.lstrip('MODIFIED: ')
        else:
            raise ShortyError(data)

    # check if the given tag is taken
    # returns true if available false if taken
    def check(self, tag):
        resp = request('http://fon.gs/check.php', {'linkname': tag})
        data = resp.read()
        if data.startswith('AVAILABLE'):
            return True
        elif data.startswith('TAKEN'):
            return False
        else:
            raise ShortyError(data)

    def expand(self, tinyurl):
        if tinyurl[-1] != '/':
            turl = tinyurl + '/'
        else:
            turl = tinyurl
        return Service.expand(self, turl)

