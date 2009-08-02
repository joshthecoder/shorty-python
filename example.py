import shorty

# A long url that needs to be shorten.
url = 'http://test.com/a/long/url/that/needs/to/be/shorten'

# The service to use for shortening the URL
# see README for list of supported services.
# For this example we will use the sandbox service
# which stores the links locally in memory.
service = 'sandbox'

# Pass in the service and long url to get a tiny url.
tinyurl = shorty.shrink(service, url)

# You could also access a global instance of the service directly.
tinyurl = shorty.sandbox.shrink(url)

# If you want a new instance of the service.
mysandbox = shorty.Sandbox()
mysandbox.shrink(url)

# If you require a list of all supported services
# for displaying in your UI as a dropdown menu or such
supported_services = shorty.services.keys()

