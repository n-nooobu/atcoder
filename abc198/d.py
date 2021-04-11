import io
import sys

# input here
_INPUT = """\
send
more
money
"""
sys.stdin = io.StringIO(_INPUT)



import itertools

S1 = input()
S2 = input()
S3 = input()

alphabets = set()
for s in [S1, S2, S3]:
    for i in s:
        alphabets.add(i)
alphabets = list(alphabets)

if len(alphabets) > 10:
    print('UNSOLVABLE')
    exit()


