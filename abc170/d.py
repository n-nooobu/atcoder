N = int(input())
A = list(map(int, input().split(' ')))

A.sort()
A.append(0)
dp = [True] * (10 ** 6 + 5)
ans = 0
for i in range(N):
    if dp[A[i]-1]:
        if A[i] != A[i + 1]:
            ans += 1
        dp[A[i]-1::A[i]] = [False] * (len(dp) // A[i])

print(ans)
