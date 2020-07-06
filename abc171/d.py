N = int(input())  # N
A = list(map(int, input().split(' ')))  # A1 A2 A3 ... An
Q = int(input())
BC = [list(map(int, list(input().split(' ')))) for i in range(Q)]

count = [0] * (10**5 + 5)
for i in range(N):
    count[A[i]] += 1

s = sum(A)
for i in range(Q):
    s = s - BC[i][0] * count[BC[i][0]] + BC[i][1] * count[BC[i][0]]
    count[BC[i][1]] += count[BC[i][0]]
    count[BC[i][0]] = 0
    print(s)
