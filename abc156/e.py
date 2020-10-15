import io
import sys

# input here
_INPUT = """\
15 6

"""
sys.stdin = io.StringIO(_INPUT)



n, k = map(int, input().split())

mod = 10 ** 9 + 7

if k >= n - 1:
    bunsi = 1
    for i in range(n - 1):
        bunsi = bunsi * (2 * n - 1 - i) % mod
    bunbo = 1
    for i in range(n - 1):
        bunbo = bunbo * (i + 1) % mod
    comb = bunsi * pow(bunbo, mod - 2, mod) % mod
    print(comb)
else:
    
