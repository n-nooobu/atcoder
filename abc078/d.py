import io
import sys

# input here
_INPUT = """\
1 1 1
1000000000

"""
sys.stdin = io.StringIO(_INPUT)



N, Z, W = map(int, input().split())
a = list(map(int, input().split()))

if N == 1:
    print(abs(a[0] - W))
else:
    print(max(abs(a[-1] - W), abs(a[-1] - a[-2])))
