import io
import sys

# input here
_INPUT = """\
2

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

if N % 2 == 1:
    print('Black')
else:
    print('White')
