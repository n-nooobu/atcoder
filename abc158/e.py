import io
import sys

# input here
_INPUT = """\
20 11
33883322005544116655


"""
sys.stdin = io.StringIO(_INPUT)



from collections import Counter

N, P = map(int, input().split())
S = input()

mod = P

ans = 0
if P == 2:
    for i in range(N):
        if int(S[i]) % 2 == 0:
            ans += i + 1
elif P == 5:
    for i in range(N):
        if int(S[i]) % 5 == 0:
            ans += i + 1
else:
    ten = [1] * N
    for i in range(1, N):
        ten[i] = ten[i - 1] * 10 % mod

    l = [0] * (N + 1)
    for i in range(1, N + 1):
        l[i] = (int(S[-i]) * ten[i - 1] + l[i - 1]) % mod

    c = Counter(l)
    for i in c:
        if c[i] > 1:
            ans += c[i] * (c[i] - 1) // 2

print(ans)
