#! /usr/bin/env python
# Parsing and creating files using  regular expressions
import sys
import re

def find_pattern(in_stream, target_regex,
        start_regex = None,
        stop_regex = None):
    """
    Reads over all matching regex found 'in_stream'.
    """

    search_started = False
    if not start_regex:
        search_started = True
    for line_index, line in enumerate(in_stream):
        if stop_regex and stop_regex.match(line):
            break
        if start_regex and (not search_started):
            if start_regex.match(line):
                search_started = True
            continue
        for match_object in target_regex.finditer(line):
            yield line_index, match_object

def record_all_occurrences(in_stream, out_stream,
        target_regex,
        start_regex = None,
        stop_regex = None):
    num_occurrences = 0
    for line_index, match_obj in find_pattern(in_stream, target_regex,
            start_regex, stop_regex):
        num_occurrences += 1
        for target_str in match_obj.groups():
            out_stream.write("{line_num}\t{string}\n".format(
                    line_num = line_index + 1,
                    string = target_str))
    return num_occurrences


if __name__ == '__main__':
    target_pattern = re.compile(r'(\w*herit\w*)', re.IGNORECASE)
    start_pattern = re.compile(r'^\*\*\*\s*START.*$')
    stop_pattern = re.compile(r'^\*\*\*\s*END.*$')
    in_path = "origin.txt"
    out_path = "output.txt"
    with open(in_path, 'r') as in_stream:
        with open(out_path, 'w') as out_stream:
            num_occurrences = record_all_occurrences(in_stream = in_stream,
                    out_stream = out_stream,
                    target_regex = target_pattern,
                    start_regex = start_pattern,
                    stop_regex = stop_pattern)
    message = "Total patterns matching heritability {0} times!".format(
            num_occurrences)
    print(message)
