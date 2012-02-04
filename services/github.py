## Shorty
## Copyright 2012 Andrea Stagi
## See LICENSE

## @url git.io
class Github(Service):

    def shrink(self, bigurl):
        gitio_pattern = 'http(s)?://((gist|raw|develop(er)?)\.)?github\.com'
        gitio_re = re.compile(gitio_pattern)
        if not gitio_re.search(bigurl):
            raise ShortyError('URL must match %s' % gitio_pattern)
        resp = request('http://git.io', post_data="url=%s" % bigurl)
        for header in resp.info().headers:
            if header.startswith("Location:"):
                return header[10:].strip('\n\r')
        raise ShortyError('Failed to shrink url')
