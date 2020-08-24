X, K, D = map(int, input().split())
X = abs(X)

sho = X // D
yo = X % D

if sho > K:
    print(X - K * D)
elif sho == K:
    print(yo)
else:
    if (K - sho) % 2 == 0:
        print(yo)
    else:
        print(abs(yo - D))
