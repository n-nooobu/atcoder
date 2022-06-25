import io
import sys

# input here
_INPUT = """\
30 123456789
LRULURLURLULULRURRLRULRRRUURRU

"""
sys.stdin = io.StringIO(_INPUT)



N, X = map(int, input().split())
S = input()

for s in S:
    if s == 'U':
        X //= 2
    elif s == 'L':
        X *= 2
    else:
        X = X * 2 + 1

print(X)
