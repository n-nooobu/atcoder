import io
import sys

# input here
_INPUT = """\
8 1
4 2 4 2 4 2 4 2

"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())
A = list(map(int, input().split()))

if N == 1:
    if A[0] % K == 1:
        print(1)
    else:
        print(0)
    exit()

cum = [0] * (N + 1)
for i in range(1, N + 1):
    cum[i] = cum[i - 1] + A[i - 1]

l = [0] * (N + 1)
for i in range(N + 1):
    l[i] = (cum[i] - i) % K

count = {}
for i in range(min(N, K)):
    try:
        count[str(l[i])] += 1
    except KeyError:
        count[str(l[i])] = 1
ans = 0
key = list(count.keys())
for i in range(len(key)):
    ans += count[key[i]] * (count[key[i]] - 1) // 2
for i in range(N + 1 - K):
    count[str(l[i])] -= 1
    try:
        ans += count[str(l[i + K])]
    except KeyError:
        pass
    try:
        count[str(l[i + K])] += 1
    except KeyError:
        count[str(l[i + K])] = 1

print(ans)
