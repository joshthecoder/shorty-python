## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url a.gd
class Agd(Service):

    def shrink(self, bigurl, tag=None, password=None, expires=None):
        post_param = {'url': bigurl}
        if tag:
            post_param['tag'] = tag
        if password:
            post_param['pass'] = password
        if expires:
            post_param['validTill'] = expires
        resp = request('http://a.gd/?module=ShortURL&file=Add&mode=API',
                        post_data = urlencode(post_param))
        url = resp.read()
        if url.startswith('http://'):
            return url
        else:
            raise ShortyError(url[url.find('>')+1:url.rfind('<')])

