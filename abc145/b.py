import io
import sys

# input here
_INPUT = """\
6
abcadc



"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
S = input()

if S[:N // 2] == S[N // 2:]:
    print('Yes')
else:
    print('No')
