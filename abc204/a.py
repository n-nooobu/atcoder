import io
import sys

# input here
_INPUT = """\
0 0

"""
sys.stdin = io.StringIO(_INPUT)



x, y = map(int, input().split())

if x == y:
    print(x)
else:
    print(3 - x - y)
