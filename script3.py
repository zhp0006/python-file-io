#!/usr/bin/env python
import re
lines = []
linenum = 0
filename = "origin.txt"
pattern = re.compile(r"inherit\B", re.IGNORECASE)
with open(filename, "rt") as myfile:
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:
            lines.append((linenum, line.rstrip('\n')))
for l in lines:
    print((str(l[0]), ":" +l[1]), file = open("output.txt", "a"))
