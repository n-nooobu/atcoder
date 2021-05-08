import io
import sys

# input here
_INPUT = """\
8
199 100 200 400 300 500 600 200


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))

a = [0] * 200
for i in range(N):
    a[A[i] % 200] += 1
ans = 0
for i in a:
    ans += i * (i - 1) // 2

print(ans)
