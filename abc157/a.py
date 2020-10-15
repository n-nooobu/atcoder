import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

if N % 2:
    print(N // 2 + 1)
else:
    print(N // 2)
