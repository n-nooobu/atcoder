import io
import sys

# input here
_INPUT = """\
630 940 314

"""
sys.stdin = io.StringIO(_INPUT)



A, B, C = map(int, input().split())

ans = -1
for i in range(1, 1001):
    if A <= i <= B and i % C == 0:
        ans = i

print(ans)
