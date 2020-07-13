N = int(input())

ans = [0] * (N + 5)
for x in range(1, 101):
    for y in range(1, 101):
        for z in range(1, 101):
            tmp = x**2 + y**2 + z**2 + x*y + y*z + z*x
            if tmp <= N:
                ans[tmp] += 1

for i in range(1, N+1):
    print(ans[i])
