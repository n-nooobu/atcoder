import io
import sys

# input here
_INPUT = """\
8
2
0
1
6
0
8
2
1


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

ans = 0
t = 0
for i in range(N-1):
    if A[i]:
        t += A[i] // 2
        if A[i] % 2 and A[i+1]:
            t += 1
            A[i+1] -= 1
    else:
        ans += t
        t = 0
t += A[-1] // 2
ans += t

print(ans)
