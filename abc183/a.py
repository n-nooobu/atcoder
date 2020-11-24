import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



x = int(input())

if x >= 0:
    print(x)
else:
    print(0)
