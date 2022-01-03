import io
import sys

# input here
_INPUT = """\
8
12 23 34 45 56 78 89 98

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))

xor = 0
for i in range(N):
    xor ^= A[i]

if xor in A:
    print('Win')
else:
    if N % 2:
        print('Win')
    else:
        print('Lose')
