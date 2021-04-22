import io
import sys

# input here
_INPUT = """\
10

"""
sys.stdin = io.StringIO(_INPUT)



import itertools

N = int(input())

for i in itertools.product(['(', ')'], repeat=N):
    c = 0
    s = ''
    for j in range(N):
        s += i[j]
        if i[j] == '(':
            c += 1
        else:
            c -= 1
        if c < 0:
            break
    if c == 0:
        print(s)
