## Shorty
## Copyright 2009 Joshua Roesslein
## See LICENSE

## @url fwd4.me
class Fwd4me(Service):

    ecodes = {
        '1': 'Invalid long url',
        '2': 'Invalid api key',
        '3': 'Account suspended or revoked',
        '4': 'Long url is black listed',
        '5': 'Internal system error'
    }

    def shrink(self, bigurl):
        resp = request('http://api.fwd4.me/', {'url': bigurl})
        data = resp.read()
        if data.startswith('ERROR:'):
            ecode = data.lstrip('ERROR:')
            raise ShortyError(Fwd4me.ecodes.get(ecode, 'Unkown error'))
        else:
            return data

