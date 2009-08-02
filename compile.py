# Shorty module compiler
# Copyright 2009 Joshua Roesslein
# See LICENSE

import sys
import os

_services = dict()

# remove any template comments
def remove_comments(text):

    output = str()
    for line in text.splitlines():
        if line.startswith('##'): continue
        output += line + '\n'
    return output

# process module source
def process_module(name, source):

    output = str()

    # iterate through source and process any @ tags
    for line in source.splitlines():
        if line.startswith('##'):
            # is a url tag?
            pos = line.find('@url')
            if pos >= 0:
                urls = line[pos+4:].split()
                _services.update(dict((url.strip(), name) for url in urls))
                output += '# %s\n' % name
        else:
            output += line + '\n'

    # write out service global instance
    output += '%s = %s()\n' % (name, name.capitalize())

    return output

def compile_shorty(services):

    # open shorty.py file
    sfp = open('shorty.py', 'w')

    # write out the header (license/ascii art/etc)
    header = open('header', 'r')
    sfp.write(header.read())
    header.close()

    # write out imports
    imports = open('imports.py', 'r')
    sfp.write(remove_comments(imports.read()))
    imports.close()

    # write out common code
    common = open('common.py', 'r')
    sfp.write(remove_comments(common.read()))
    common.close()

    # write service module code
    for service in services:
        try:
            module = open('services/%s.py' % service, 'r')
        except IOError:
            print '%s not found! Skipping' % service
            continue

        sfp.write(process_module(service, module.read()))
        module.close()

    # write out services dict
    sfp.write('\nservices = {\n')
    for k,v in _services.items():
        sfp.write("    '%s': %s,\n" % (k,v))
    sfp.write('}\n\n')

    sfp.close()

if __name__ == '__main__':

    # make sure enough args are provided
    if len(sys.argv) < 2:
        print 'Usage: compile.py <services>'
        print '  services -- names of the services to include in compiled module'
        print 'Example: compile.py sandbox tinyurl bitly'
        sys.exit(1)

    # get list of services to compile
    if sys.argv[1] == '--all':
        services = list(m.split('.')[0] for m in os.listdir('services'))
    else:
        services = sys.argv[1:]

    # compile shorty
    compile_shorty(services)

