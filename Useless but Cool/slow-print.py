#!/usr/bin/python3
import sys
from time import sleep

file = sys.argv[1]

with open(file, 'r') as a_string:
    for line in a_string:
        for letter in line:
            sys.stdout.write(letter)
            sys.stdout.flush()
            sleep(0.025)


sys.stdout.write('\n')