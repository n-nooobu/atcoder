import io
import sys

# input here
_INPUT = """\
4 9 26
"""
sys.stdin = io.StringIO(_INPUT)



a, b, c = map(int, input().split())

if a + b > c:
    print('No')
else:
    if 4 * a * b < (c - a - b) ** 2:
        print('Yes')
    else:
        print('No')
