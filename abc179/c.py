import io
import sys

# input here
_INPUT = """\
100
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

ans = 0
for i in range(1, N):
    sho = (N - 1) // i
    ans += sho

print(ans)
