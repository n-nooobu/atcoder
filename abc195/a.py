import io
import sys

# input here
_INPUT = """\
10 125


"""
sys.stdin = io.StringIO(_INPUT)


M, H = map(int, input().split())

if H % M == 0:
    print('Yes')
else:
    print('No')
