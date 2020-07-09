import itertools

H, W, K = map(int, input().split())
c = [list(str(input())) for i in range(H)]

ans = 0
for i in itertools.product(range(2), repeat=H+W):
    cnt = 0
    for j in itertools.product(range(H), range(W)):
        if i[j[0]]:
            continue
        if i[H+j[1]]:
            continue
        if c[j[0]][j[1]] == '#':
            cnt += 1
    if cnt == K:
        ans += 1

print(ans)
