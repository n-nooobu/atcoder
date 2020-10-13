import io
import sys

# input here
_INPUT = """\
8
1 2 1 4 2 1 4 1

"""
sys.stdin = io.StringIO(_INPUT)



from collections import Counter

N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
combination = [0] * (N + 1)
for i in c:
    combination[i] = c[i] * (c[i] - 1) // 2

s = sum(combination)
for i in range(N):
    ans = s - combination[A[i]] + (c[A[i]] - 1) * (c[A[i]] - 2) // 2
    print(ans)
