import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
P = list(map(int, input().split()))
I = list(map(int, input().split()))

ans = [[0, 0] for _ in range(N)]

p_idx = 0
i_idx = 0
now = 0
while p_idx < N or i_idx < N:
    if now == 0:
        now = P[p_idx]
        p_idx += 1
    else:
        if now == I[i_idx]:
            i_idx += 1
