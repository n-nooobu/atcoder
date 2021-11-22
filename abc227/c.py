import io
import sys

# input here
_INPUT = """\
100000000000

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

ans = 0
for a in range(1, 5 * 10 ** 3):
    bc = N // a
    for b in range(a, int(bc ** (1 / 2)) + 1):
        c = N // (a * b)
        ans += max(0, c - b + 1)

print(ans)
