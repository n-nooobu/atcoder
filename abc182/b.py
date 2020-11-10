import io
import sys

# input here
_INPUT = """\
5
1000 1000 1000 1000 1000

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))

ans = [0, 0]
for i in range(2, max(A) + 1):
    gcd = 0
    for j in range(N):
        if A[j] % i == 0:
            gcd += 1
    if gcd > ans[0]:
        ans = [gcd, i]

print(ans[1])
