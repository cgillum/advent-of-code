import os
import sys
from collections import defaultdict

# Example:
# dabAcCaCBAcCcaDA  The first 'cC' is removed.
# dabAaCBAcCcaDA    This creates 'Aa', which is removed.
# dabCBAcCcaDA      Either 'cC' or 'Cc' are removed (the result is the same).
# dabCBAcaDA        No further actions can be taken.

def cancelling(c1, c2):
    return abs(ord(c1) - ord(c2)) == 32

def char_range(c1, c2):
    for i in range(ord(c1), ord(c2)+1):
        yield chr(i)

def reduce(s):
    i = 1
    while i < len(s):
        curr = s[i]
        prev = s[i - 1]
        if cancelling(curr, prev):
            remove = s[i-1:i+1]
            s = s.replace(remove, '')
            if i > 1: i -= 1
        else:
            i += 1
    return s

with open(os.path.join(sys.path[0], 'day05-input.txt')) as file:
    for line in file:
        s = line[:-1]
        print(f'Starting length: {len(s)}')
        result = reduce(s)
        print(f'Part 1 - Ending length: {len(result)}') # 9288

        # Part 2: What is the length of the shortest polymer you can produce 
        # by removing all units of exactly one type and fully reacting the result?
        chars = {}
        for c in char_range('a', 'z'):
            variant = s.replace(c, '').replace(chr(ord(c) - 32), '')
            chars[c] = len(reduce(variant))

        winner = min(chars.items(), key = lambda pair: pair[1])
        print(f'Part 2 - Best removal is "{winner[0]}" with length {winner[1]}')

        
        

