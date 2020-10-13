import io
import sys

# input here
_INPUT = """\
1 2
3 3
3

"""
sys.stdin = io.StringIO(_INPUT)



A, V = map(int, input().split())
B, W = map(int, input().split())
T = int(input())

if V <= W:
    print('NO')
elif (V - W) * T >= abs(A - B):
    print('YES')
else:
    print('NO')
