#!/usr/bin/env python


import re
filename = "origin.txt"
pattern = re.compile(r"^inherit", re.IGNORECASE)
with open(filename, "rt") as myfile:
    for line in myfile:
        if pattern.search(line) != None:
            print(line, end='')
