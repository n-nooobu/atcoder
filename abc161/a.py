import io
import sys

# input here
_INPUT = """\
1 2 3
"""
sys.stdin = io.StringIO(_INPUT)



X, Y, Z = map(int, input().split())

print(Z, X, Y)
