import io
import sys

# input here
_INPUT = """\
1000000
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

ans = 0
for i in range(1, N + 1):
    if i % 3 != 0 and i % 5 != 0:
        ans += i

print(ans)
