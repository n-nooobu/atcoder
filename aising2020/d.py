N = int(input())
X = int(str(input()), 2)
X_bin = format(X, '0'+str(N)+'b')
popcount = [X_bin.count('1') - 1, X_bin.count('1') + 1]
mod = [X % popcount[0], X % popcount[1]]

ans = [0] * N
for i in range(N):
    if X_bin[i] == '1':
        if X_bin.count('1') == 1:
            print(0)
            continue
        n = mod[0] - (2**(N-1-i)) % popcount[0]
        if n == popcount[0]:
            print(1)
            continue
    else:
        n = mod[1] + (2**(N-1-i)) % popcount[1]
        if n == popcount[1]:
            print(1)
            continue
    ans[i] += 1
    while n != 0:
        n = n % format(n, '0'+str(N)+'b').count('1')
        ans[i] += 1

    print(ans[i])
