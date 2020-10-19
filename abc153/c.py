import io
import sys

# input here
_INPUT = """\
3 0
1000000000 1000000000 1000000000

"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
H = list(map(int, input().split()))

H = sorted(H)
if K != 0:
    print(sum(H[:-K]))
else:
    print(sum(H))
