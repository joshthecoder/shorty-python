## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url short.ie
class Shortie(Service):

    def __init__(self, email=None, secretkey=None):
        self.email = email
        self.secretkey = secretkey

    def _test(self):
        # prompt for email and key
        self.email = raw_input('shortie email: ')
        self.secretkey = raw_input('shortie secretKey: ')

        Service._test(self)

    def shrink(self, bigurl, tag=None, private=False):
        if self.email is None or self.secretkey is None:
            raise ShortyError('Must provide an email and secretkey')
        parameters = {
            'email': self.email, 'secretKey': self.secretkey,
            'format': 'json',
            'url': bigurl
        }
        if tag:
            parameters['custom'] = tag
        if private:
            parameters['private'] = 'true'
        resp = request('http://short.ie/api', parameters)
        jdata = json.loads(resp.read())['short']
        if jdata['error']['code'] != 0:
            raise ShortyError(jdata['error']['msg'])
        return str(jdata['shortened'])

