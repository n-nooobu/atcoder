import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



S = input()

if S[2] == S[3] and S[4] == S[5]:
    print('Yes')
else:
    print('No')
