import io
import sys

# input here
_INPUT = """\
12 6
"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())

if N % 2 == 1:
    for i in range(M):
        print(N // 2 - i, N // 2 + 1 + i)
else:
    if N == 4:
        print(2, 3)
    elif N // 2 % 2 == 1:
        for i in range(M - 1):
            print(N // 2 - 1 - i, N // 2 + 1 + i)
        print(N // 2, N)
    else:
        for i in range(M - 2):
            print((N - 2) // 2 - 1 - i, (N - 2) // 2 + 1 + i)
        print((N - 2) // 2, N - 2)
        print(N - 1, N)
