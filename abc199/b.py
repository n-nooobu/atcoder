import io
import sys

# input here
_INPUT = """\
3
3 2 5
6 9 8


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mi = 1
ma = 1000
for i in range(N):
    mi = max(mi, A[i])
    ma = min(ma, B[i])

print(max(0, ma - mi + 1))
