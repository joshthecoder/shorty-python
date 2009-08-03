## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url sandbox.com
## used for testing
class Sandbox(Service):

    def __init__(self, length=4, letters='abcdefghijklmnopqrstuvwxyz'):
        self.urls = {}
        self.letters = letters
        self.length = length
        self.base = len(letters) - 1

    def shrink(self, bigurl):
        # generate the tiny path
        tpath = ''
        while True:
            for i in range(self.length):
                tpath += self.letters[randint(0, self.base)]
            if self.urls.has_key(tpath):
                # tpath already in use, regen another
                tpath = ''
            else:
                break

        # store url and return tiny link
        self.urls[tpath] = bigurl
        return 'http://sandbox.com/' + tpath

    def expand(self, tinyurl):
        # lookup big url and return
        turl = urlparse(tinyurl)
        if turl[1] != 'sandbox.com':
            raise ShortyError('Not a sandbox url')
        return self.urls.get(turl[2].strip('/'))

