import shorty

# a long url that needs to be shorten
url = 'http://test.com/a/long/url/that/needs/to/be/shorten'

# The service to use for shortening the URL
# see README for list of supported services.
# For this example we will use the sandbox service
# which stores the links locally in memory.
service = 'sandbox'

# pass in the service and long url to get a tiny url
tinyurl = shorty.shrink(service, url)
