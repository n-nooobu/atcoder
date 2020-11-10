import io
import sys

# input here
_INPUT = """\
2525 -425

"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())

if K >= 0:
    patern = 2 * N - 1 - K
else:
    patern = 2 * N - 1 + K

def cal(N, n):
    if n % 2 == 0:
        return (N - n // 2) * 2 + 1
    else:
        return (N - n // 2) * 2

ans = 0
if K >= 0:
    for i in range(2, patern + 2):

        ans += cal(min(N, i - 1), i) * cal(min(N, i + K - 1), i + K)
else:
    for i in range(2 - K, patern + 2 - K):
        ans += cal(min(N, i - 1), i) * cal(min(N, i + K - 1), i + K)

print(ans)
