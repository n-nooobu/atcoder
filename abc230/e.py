import io
import sys

# input here
_INPUT = """\
2
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

k = 1
i = N
ans = 0
while k <= N:
    next_i = N // (k + 1)
    ans += k * (i - next_i)
    i = next_i
    if i == 0:
        break
    k = N // i

print(ans)
