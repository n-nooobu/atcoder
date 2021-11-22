import io
import sys

# input here
_INPUT = """\
3 14 15926535

"""
sys.stdin = io.StringIO(_INPUT)



N, K, M = map(int, input().split())
mod = 998244353

if M % mod != 0:
    a = pow(K, N, mod - 1)
    print(pow(M, a, mod))
else:
    print(0)
