import io
import sys

# input here
_INPUT = """\
7
1 2 3 4 5 6
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = [0] * 2 + list(map(int, input().split()))

l = [0] * (N + 1)
for i in range(2, N + 1):
    l[A[i]] += 1

for i in range(1, N + 1):
    print(l[i])
