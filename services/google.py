## Shorty
## Copyright 2011 Andrea Stagi
## See LICENSE

## @url goo.gl
class Google(Service):

    def shrink(self, bigurl):
        resp = request('https://www.googleapis.com/urlshortener/v1/url', 
                        headers={"content-type":"application/json"}, 
                        post_data=json.dumps({"longUrl": bigurl}))
        data = resp.read()
        jdata = json.loads(data)
        if 'id' not in jdata:
            raise ShortyError(data)
        else:
            return jdata['id']

    def qrcode(self, tinyurl):
        qrdata = request(tinyurl + '.qr').read()
        return qrdata

