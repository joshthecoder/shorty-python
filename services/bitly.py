## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url bit.ly
class Bitly(Service):

    version = '2.0.1'

    def __init__(self, login=None, apikey=None, password=None):
        self.login = login
        self.apikey = apikey
        self.password = password

    def _test(self):
        # prompt for login
        self.login = raw_input('bitly login: ')
        
        # ask if tester wants to provide apikey or password
        print 'auth with password(P) or apikey(K)?'
        if raw_input() == 'P':
            self.password = getpass('bitly password: ')
        else:
            self.apikey = raw_input('bitly apikey: ')

        Service._test(self)

    def _setup(self):
        parameters = {'version': self.version}
        if self.apikey:
            parameters['apiKey'] = self.apikey
            parameters['login'] = self.login
            username_pass = None
        elif self.password:
            username_pass = (self.login, self.password)
        else:
            raise ShortyError('Must set an apikey or password')
        return parameters, username_pass

    def shrink(self, bigurl):
        if not self.login:
            raise ShortyError('Must set a login')
        parameters, username_pass = self._setup()
        parameters['longUrl'] = bigurl
        resp = request('http://api.bit.ly/shorten', parameters, username_pass)
        jdata = json.loads(resp.read())
        if jdata['errorCode'] != 0:
            raise ShortyError(jdata['errorMessage'])
        return str(jdata['results'][bigurl]['shortUrl'])

    def expand(self, tinyurl):
        if not self.login:
            return get_redirect(tinyurl)
        parameters, username_pass = self._setup()
        parameters['shortUrl'] = tinyurl
        resp = request('http://api.bit.ly/expand', parameters, username_pass)
        jdata = json.loads(resp.read())
        if jdata['errorCode'] != 0:
            raise ShortyError(jdata['errorMessage'])
        return str(jdata['results'].values()[0]['longUrl'])

    def stats(self, tinyurl):
        if not self.login:
            return get_redirect(tinyurl)
        parameters, username_pass = self._setup()
        parameters['shortUrl'] = tinyurl
        resp = request('http://api.bit.ly/v3/clicks', parameters, username_pass)
        jdata = json.loads(resp.read())
        if jdata['status_code'] != 200:
            raise ShortyError(jdata['errorMessage'])
        clicks = {}
        clicks['user'] = jdata['data']['clicks'][0]['user_clicks']
        clicks['global'] = jdata['data']['clicks'][0]['global_clicks']
        return clicks

    def qrcode(self, tinyurl):
        qrdata = request(tinyurl + '.qrcode').read()
        return qrdata

