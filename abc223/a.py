import io
import sys

# input here
_INPUT = """\
0

"""
sys.stdin = io.StringIO(_INPUT)



X = int(input())

if X % 100 == 0 and X >= 100:
    print('Yes')
else:
    print('No')
