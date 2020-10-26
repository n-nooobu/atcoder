import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



A, B, C = map(int, input().split())

if A == B or B == C or C == A:
    if A == B == C:
        print('No')
    else:
        print('Yes')
else:
    print('No')
