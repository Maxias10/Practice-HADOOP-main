#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    key_value = line.split(',')
    program = key_value[0]
    print(f'{program}\t1')
