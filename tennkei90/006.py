import io
import sys

# input here
_INPUT = """\
14 5
kittyonyourlap


"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
S = input()

a = {chr(ord('a')+i): i for i in range(26)}
b = [[-1] * N for _ in range(26)]
c = [-1] * 26

for i in range(N-1, -1, -1):
    c[a[S[i]]] = i
    for j in range(26):
        b[j][i] = c[j]

i = 0
k = 0
ans = ''
while k < K:
    for j in range(26):
        if 0 <= b[j][i] <= N - (K - k):
            ans = ans + chr(ord('a')+j)
            i = b[j][i] + 1
            k += 1
            break

print(ans)
