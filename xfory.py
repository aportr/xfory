#!/usr/bin/env python

import random

words = [
    'the cloud',
    'Twitter',
    'big data',
    'Facebook',
    'Tinder',
    'LinkedIn',
    'Service Oriented Architecture (SOA)',
    'Infrastructure',
    'Infrastructure-as-a-service (IaaS)',
    'Yelp',
    'People',
    'Snapchat',
    'music',
    'Shazam',
    'Kazaam',
    'Skype',
    'sandwiches',
    'geese',
    'Uber drivers',
    'scuba divers',
    'email',
    'Top Gear',
    'camping',
    'sausages',
    'coffee',
    'configuration management',
    'AWS',
    'serverless',
    'LISP',
    'sql injection',
    'polymorphism',
    'bittorrent',
    'bitcoin',
    'bitchain',
    'singele sign on',
    'intrusion detection systems',
    'hash collisons',
    'Big O notation',
    'IPv6',
    'DNS',
    'the kernel',
    'design patterns',
    'devops',
    'test driven development',
    'agile',
    'lean',
    'the enterprise',
    'bash',
    'javascript',
    'assembly',
    'open source',
    'GCC',
    'GNU',
    'Linux',
    'Windows',
    'continuous integration',
    'Address Space Layout Randomisation',
    'popping calc',
    'the internet of things',
    'dependency management',
    'package management',
    'Stack overflow',
    'heapsort',
    'quicksort',
    'bubblesort',
    'the BIOS',
    'AHCI',
    'hard drives',
    'data mining',
    'RAID',
    'PHP',
    'segfaults'
]
x = random.choice(words)
y = random.choice(words)

print "Content-Type: text/html"
print
print "<!DOCTYPE html>"
print "<head><title>It's like X for Y</title></head>"
print "<body>"
print "It\'s like %s for %s." % (x, y)
print "</body>"

