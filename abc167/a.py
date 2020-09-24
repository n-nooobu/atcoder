import io
import sys

# input here
_INPUT = """\
chokudai
chokudaiz
"""
sys.stdin = io.StringIO(_INPUT)



S = input()
T = input()

if T[:-1] == S:
    print('Yes')
else:
    print('No')
