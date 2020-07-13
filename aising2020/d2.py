from random import randint

#N = randint(1, 2*(10**5))
#N = int(input())
N = 2*(10**5)
#X = randint(1, 2**(N+1)-1)
#X = int(str(input()), 2)
X = 2**(N+1)-1
X_bin = format(X, '0'+str(N)+'b')
popcount = [X_bin.count('1') - 1, X_bin.count('1') + 1]
mod = [X % popcount[0], X % popcount[1]]

ans = [0] * N
dp = [0] * 2 ** 18
for i in range(N):
    if X_bin[i] == '1':
        if X_bin.count('1') == 1:
            ans[i] = 0
            print(ans[i])
            continue
        n = mod[0] - (2 ** (N - 1 - i)) % popcount[0]
        if n == popcount[0]:
            ans[i] = 1
            print(ans[i])
            continue
        elif n < 0:
            n += popcount[0]
    else:
        n = mod[1] + (2 ** (N - 1 - i)) % popcount[1]
        if n == popcount[1]:
            ans[i] = 1
            print(ans[i])
            continue

    tmp = []
    ans[i] += 1
    while n != 0:
        if dp[n]:
            ans[i] += dp[n]
            break
        tmp.append(n)
        n = n % format(n, '0' + str(N) + 'b').count('1')
        ans[i] += 1
    for j in range(len(tmp)):
        dp[tmp[j]] = ans[i] - 1 - j

    print(ans[i])