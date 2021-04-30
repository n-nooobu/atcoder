import io
import sys

# input here
_INPUT = """\
5 1
"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())

if M < 0 or M == N or (M == N - 1 and N >= 2):
    print(-1)
elif M == 0:
    for i in range(1, 2*N, 2):
        print(i, i+1)
else:
    print(1, 2*(M+1)+2)
    for i in range(2, 2*(M+1)+1, 2):
        print(i, i+1)
    for i in range(2*(M+1)+3, 2*(M+1)+3 + 2*(N-(M+2)), 2):
        print(i, i+1)
