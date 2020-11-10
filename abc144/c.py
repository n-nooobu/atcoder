import io
import sys

# input here
_INPUT = """\
10000000019

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

ans = 10 ** 18
for i in range(1, round(N ** 0.5) + 1):
    if N % i == 0:
        ans = min(ans, i - 1 + N // i - 1)

print(ans)
