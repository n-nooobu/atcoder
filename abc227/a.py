import io
import sys

# input here
_INPUT = """\
3 14 2

"""
sys.stdin = io.StringIO(_INPUT)



N, K, A = map(int, input().split())

hito = A + K - 1
hito %= N

if hito == 0:
    print(N)
else:
    print(hito)
