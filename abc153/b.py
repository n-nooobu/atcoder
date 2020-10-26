import io
import sys

# input here
_INPUT = """\
210 5
31 41 59 26 53

"""
sys.stdin = io.StringIO(_INPUT)



H, N = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) >= H:
    print('Yes')
else:
    print('No')
