import io
import sys

# input here
_INPUT = """\
1
11 11
"""
sys.stdin = io.StringIO(_INPUT)



import sys

K = int(input())
A, B = map(int, input().split())

t = K
while t <= 1000:
    if A <= t <= B:
        print('OK')
        sys.exit()
    t += K

print('NG')
