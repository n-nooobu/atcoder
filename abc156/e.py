import io
import sys

# input here
_INPUT = """\
15 6

"""
sys.stdin = io.StringIO(_INPUT)



n, k = map(int, input().split())

mod = 10 ** 9 + 7

def combination(n, r):
    bunsi = 1
    for i in range(r):
        bunsi = bunsi * (n - i) % mod
    bunbo = 1
    for i in range(r):
        bunbo = bunbo * (i + 1) % mod
    comb = bunsi * pow(bunbo, mod - 2, mod) % mod
    return comb

all_ = combination(2 * n - 1, n - 1)
if k >= n - 1:

else:
    
