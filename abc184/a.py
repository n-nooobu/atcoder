import io
import sys

# input here
_INPUT = """\
0 -1
1 0

"""
sys.stdin = io.StringIO(_INPUT)



a, b = map(int, input().split())
c, d = map(int, input().split())

print(a * d - b * c)
