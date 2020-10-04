import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



S, W = map(int, input().split())

if S <= W:
    print('unsafe')
else:
    print('safe')
