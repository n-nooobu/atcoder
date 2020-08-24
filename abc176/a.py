N, X, T = map(int, list(input().split()))

if N % X == 0:
    print(N // X * T)
else:
    print(N // X * T + T)