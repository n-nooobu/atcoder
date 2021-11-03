import io
import sys

# input here
_INPUT = """\
4
1 1 1 1

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))

ans = [0] * N
max_idx = -1
max_value = 0
min_idx = -1
min_value = 10 ** 11
for i in range(N):
    if max_idx != -1 and min_idx != -1 and A[i] > min_value:
        ans[max_idx] = 1
        max_idx = -1
        max_value = 0
        ans[min_idx] = 1
        min_idx = -1
        min_value = 10 ** 11
    if A[i] > max_value:
        max_idx = i
        max_value = A[i]
    elif A[i] < min_value:
        min_idx = i
        min_value = A[i]
if max_idx != -1 and min_idx != -1:
    ans[max_idx] = 1
    ans[min_idx] = 1

print(*ans, sep=' ')
