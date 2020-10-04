import io
import sys

# input here
_INPUT = """\
10 10 1
1 10 9 1
"""
sys.stdin = io.StringIO(_INPUT)



import sys
sys.setrecursionlimit(10**9)

N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(Q)]

def dfs(A, ans, k):
    k += 1
    s = 0
    for q in range(Q):
        if A[abcd[q][1] - 1] - A[abcd[q][0] - 1] == abcd[q][2]:
            s += abcd[q][3]
    ans = max(ans, s)

    A[-1] += 1
    for i in reversed(range(N)):
        if A[0] == M + 1:
            return A, ans, k
        if A[i] == M + 1:
            for j in range(i, N):
                A[j] = A[i - 1] + 1
            A[i - 1] += 1

    A, ans, k = dfs(A, ans, k)
    return A, ans, k

k = 0
ans = 0
A = [1] * N

A, ans, k = dfs(A, ans, k)
print(ans)
