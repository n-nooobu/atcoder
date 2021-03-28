import io
import sys

# input here
_INPUT = """\
100000


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

ab = set()
for i in range(2, int(N ** 0.5) + 1):
    t = i ** 2
    while t <= N:
        ab.add(t)
        t *= i

print(N - len(ab))
