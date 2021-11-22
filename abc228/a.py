import io
import sys

# input here
_INPUT = """\
23 7 6

"""
sys.stdin = io.StringIO(_INPUT)



S, T, X = map(int, input().split())

if S >= T:
    T += 24
if S <= X < T or S <= X + 24 < T:
    print('Yes')
else:
    print('No')
