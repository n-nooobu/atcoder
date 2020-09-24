import io
import sys

# input here
_INPUT = """\
1333333333
"""
sys.stdin = io.StringIO(_INPUT)




import itertools

N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(Q)]


