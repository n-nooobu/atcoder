import io
import sys

# input here
_INPUT = """\
39
RBRBGRBGGBBRRGBBRRRBGGBRBGBRBGBRBBBGBBB
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
S = input()

r = [0] * N
g = [0] * N
b = [0] * N
for i in range(N):
    if i != 0:
        r[-1 - i] = r[-1 - i + 1]
        g[-1 - i] = g[-1 - i + 1]
        b[-1 - i] = b[-1 - i + 1]
    if S[-1 - i] == 'R':
        r[-1 - i] += 1
    elif S[-1 - i] == 'G':
        g[-1 - i] += 1
    else:
        b[-1 - i] += 1

ans = 0
for i in range(N):
    for j in range(i + 1, N - 1):
        if (S[i] == 'R' and S[j] == 'G') or (S[i] == 'G' and S[j] == 'R'):
            if j + j - i < N and S[j + j - i] == 'B':
                ans += b[j + 1] - 1
            else:
                ans += b[j + 1]
        elif (S[i] == 'G' and S[j] == 'B') or (S[i] == 'B' and S[j] == 'G'):
            if j + j - i < N and S[j + j - i] == 'R':
                ans += r[j + 1] - 1
            else:
                ans += r[j + 1]
        elif (S[i] == 'R' and S[j] == 'B') or (S[i] == 'B' and S[j] == 'R'):
            if j + j - i < N and S[j + j - i] == 'G':
                ans += g[j + 1] - 1
            else:
                ans += g[j + 1]

print(ans)
