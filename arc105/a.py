import io
import sys

# input here
_INPUT = """\
1 2 4 8

"""
sys.stdin = io.StringIO(_INPUT)



import sys
import itertools

A = list(map(int, input().split()))

for i in itertools.product(range(2), repeat=4):
    t = 0
    for j in range(4):
        if i[j] == 1:
            t += A[j]
    if t == sum(A) - t:
        print('Yes')
        sys.exit()

print('No')
