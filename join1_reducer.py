#!/usr/bin/env python

import sys

current_program = None
current_count = 0
program = None

for line in sys.stdin:
    line = line.strip()
    program, count = line.split('\t')
    try:
        count = int(count)
    except ValueError:
        continue
    
    if current_program == program:
        current_count += count
    else:
        if current_program:
            print(f'{current_program}\t{current_count}')
        current_program = program
        current_count = count

if current_program == program:
    print(f'{current_program}\t{current_count}')
