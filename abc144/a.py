import io
import sys

# input here
_INPUT = """\
2 5

"""
sys.stdin = io.StringIO(_INPUT)



A, B = map(int, input().split())

if 0 < A < 10 and 0 < B < 10:
    print(A * B)
else:
    print(-1)
