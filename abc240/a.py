import io
import sys

# input here
_INPUT = """\
1 10

"""
sys.stdin = io.StringIO(_INPUT)



a, b = map(int, input().split())

if (a == 1 and b == 10) or (a == 10 and b == 10) or (abs(a - b) == 1):
    print('Yes')
else:
    print('No')
