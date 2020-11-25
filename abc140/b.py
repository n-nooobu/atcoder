import io
import sys

# input here
_INPUT = """\
4
2 3 4 1
13 5 8 24
45 9 15


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = sum(B)
for i in range(N - 1):
    if A[i] + 1 == A[i + 1]:
        ans += C[A[i] - 1]

print(ans)
