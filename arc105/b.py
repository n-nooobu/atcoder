import io
import sys

# input here
_INPUT = """\
15
546 3192 1932 630 2100 4116 3906 3234 1302 1806 3528 3780 252 1008 588

"""
sys.stdin = io.StringIO(_INPUT)



from math import gcd

N = int(input())
a = list(map(int, input().split()))

g = a[0]
for i in range(1, N):
    g = gcd(g, a[i])

print(g)
