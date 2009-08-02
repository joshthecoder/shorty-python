# Shorty
# Copyright 2009 Joshua Roesslein
# See LICENSE

import shorty

print 'Running shorty tests...'

passes = 0
fails = 0

for name, service in shorty.services.items():

    try:
        if service.tested:
            # skip services with aliases
            continue
        service._test()
        passes += 1
        print 'PASS: <%s>' % name
    except shorty.ShortyError, e:
        fails += 1
        print 'FAIL: <%s> %s' % (name, e)

print 'PASSES: %i  FAILS: %i' % (passes, fails)
