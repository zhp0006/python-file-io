#!/usr/bin/env python


import re
inherit = []
linenum = 0
filename = "origin.txt"
pattern = re.compile(r"^inherit", re.IGNORECASE)
with open(filename, "rt") as myfile:
    for line in myfile:
        linenum += 1
        if pattern.search(line) != None:
            pattern.append((linenum, line.rstrip('\n')))
for inher in inherit:
     print("Line ", +str(inher[0]) + ";" +err[1])
