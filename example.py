import shorty

# a long url that needs to be shorten
url = 'http://test.com/a/long/url/that/needs/to/be/shorten'

# the service to use for shortening the URL
# see README for list of supported services
service = 'someservice'

# pass in the service and long url to get a tiny url
tinyurl = shorty.shrink(service, url)
