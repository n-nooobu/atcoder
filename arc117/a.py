import io
import sys

# input here
_INPUT = """\
7 5

"""
sys.stdin = io.StringIO(_INPUT)



A, B = map(int, input().split())

if A >= B:
    for i in range(1, A + 1):
        print(i, end=' ')
    for i in range(1, B):
        print(-i, end=' ')
    print(-((1 + A) * A // 2 - B * (B - 1) // 2))
else:
    for i in range(1, B + 1):
        print(-i, end=' ')
    for i in range(1, A):
        print(i, end=' ')
    print((1 + B) * B // 2 - A * (A - 1) // 2)
