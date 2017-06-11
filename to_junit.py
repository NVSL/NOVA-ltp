#!/usr/bin/env python

import sys
import re

lines = sys.stdin.readlines()

l = 0
max_l = len(lines)

def skipped(name):
    return ""

def success(name):
    print name
    a = re.split('\s+',name,maxsplit=2)
    return '<testcase classname="{}" name="{}"/>'.format(a[0], a[1])

def failure(name, kind, reason):
    print name
    a = re.split('\s+',name,maxsplit=2)
    return """<testcase classname="{}" name="{}">
        <failure type="{}"> {}</failure>
    </testcase>""".format(a[0], a[1], kind, reason)
    

out = []

while l < max_l:
    g = re.search("(^.*\d+)\s+T([A-Z]+)(.*)", lines[l])
    if g:
        print g.group(2)
        if g.group(2) == "PASS":
            out.append(success(g.group(1)))
        else:
            out.append(failure(g.group(1), g.group(2), g.group(3)))
            
    l += 1

print """<testsuite tests="{count}">
{tests}
</testsuite>
""".format(count=len(out), tests='\n'.join(out))
