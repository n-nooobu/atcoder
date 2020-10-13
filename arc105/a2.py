import io
import sys

# input here
_INPUT = """\
1 3 2 4

"""
sys.stdin = io.StringIO(_INPUT)



import sys
import itertools

A = list(map(int, input().split()))

for i in itertools.product(range(2), repeat=4):
    cookey = A[0] * i[0] + A[1] * i[1] + A[2] * i[2] + A[3] * i[3]
    if cookey == sum(A) - cookey:
        print('Yes')
        sys.exit()

print('No')
