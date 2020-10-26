import io
import sys

# input here
_INPUT = """\
500000000000 500000000000 1000000000000

"""
sys.stdin = io.StringIO(_INPUT)



A, B, K = map(int, input().split())

if K >= A:
    print(0, max(0, B - (K - A)))
else:
    print(A - K, B)
