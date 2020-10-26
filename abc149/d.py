import io
import sys

# input here
_INPUT = """\
30 5
325 234 123
rspsspspsrpspsppprpsprpssprpsr

"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
win = {'r': 2, 's': 0, 'p': 1}
point = [R, S, P]

ans = 0
for i in range(K):
    if i < N % K:
        dp = [[0] * 3 for _ in range(N // K + 1)]
    else:
        dp = [[0] * 3 for _ in range(N // K)]
    for j in range(3):
        if j == win[T[i]]:
            dp[0][j] = point[j]

    for j in range(1, len(dp)):
        for l in range(3):
            for m in range(3):
                if l == m:
                    continue
                if m == win[T[j * K + i]]:
                    dp[j][m] = max(dp[j][m], dp[j-1][l] + point[m])
                else:
                    dp[j][m] = max(dp[j][m], dp[j - 1][l])

    ans += max(dp[-1])

print(ans)
