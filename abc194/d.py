import io
import sys

# input here
_INPUT = """\
3
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

ans = 0
for i in range(N - 1, 0, -1):
    ans += N / i

print(ans)
