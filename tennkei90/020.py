import io
import sys

# input here
_INPUT = """\
8 3 2


"""
sys.stdin = io.StringIO(_INPUT)



a, b, c = map(int, input().split())

if a < pow(c, b):
    print('Yes')
else:
    print('No')
