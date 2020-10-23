import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())

if N == M:
    print('Yes')
else:
    print('No')
