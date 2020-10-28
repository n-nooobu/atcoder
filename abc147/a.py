import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



A = list(map(int, input().split()))

if sum(A) >= 22:
    print('bust')
else:
    print('win')
