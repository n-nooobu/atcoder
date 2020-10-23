import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



K, X = map(int, input().split())

if K * 500 >= X:
    print('Yes')
else:
    print('No')
