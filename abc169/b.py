N = int(input())
A = list(map(int, input().split(' ')))

if A.count(0):
    print(0)
else:
    ans = 1
    for i in range(N):
        ans *= A[i]
        if ans > 10 ** 18:
            break

    if ans > 10 ** 18:
        print(-1)
    else:
        print(ans)
