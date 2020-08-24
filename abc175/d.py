N, K = map(int, input().split())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

for i in range(N):
    P[i] -= 1

ans = -10 ** 18
for si in range(N):
    x = si
    c = []
    tot = 0
    while True:
        x = P[x]
        c.append(C[x])
        tot += C[x]
        if x == si:
            break

    s = 0
    for k in range(len(c)):
        if k + 1 > K:
            break
        s += c[k]
        ss = s
        if tot > 0:
            ss += tot * int((K - (k + 1)) // len(c))
        ans = max(ss, ans)

print(ans)
