import io
import sys

# input here
_INPUT = """\
41 2
5 6
"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) > N:
    print(-1)
else:
    print(N - sum(A))
