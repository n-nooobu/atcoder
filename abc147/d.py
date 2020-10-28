import io
import sys

# input here
_INPUT = """\
10
3 14 159 2653 58979 323846 2643383 27950288 419716939 9375105820

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))

mod = 10 ** 9 + 7

bit = [0] * 60
for i in range(N):
    for j in range(60):
        if A[i] & 1 << j:
            bit[j] += 1

ans = 0
for i in range(N):
    for j in range(60):
        if A[i] & 1 << j:
            bit[j] -= 1
            ans += pow(2, j) * (N - (i + 1) - bit[j])
        else:
            ans += pow(2, j) * bit[j]
        ans %= mod

print(ans)
