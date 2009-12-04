## Shorty
## Copyright 2009 Kumar Appaiah
## See LICENSE

## @url ur1.ca
class Ur1ca(Service):

    def shrink(self, bigurl):
        resp = request('http://ur1.ca/',
            post_data = urlencode({'longurl': bigurl, 'submit' : 'Make it an ur1!'}))
        returned_data = resp.read()
        matched_re = re.search('Your ur1 is: <a href="(http://ur1.ca/[^"]+)">\\1', returned_data)
        if matched_re:
            return matched_re.group(1)
        else:
            raise ShortyError('Failed to shrink url')

