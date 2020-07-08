N = int(input())
A = list(map(int, input().split()))

need = 0
for i in range(2, A):
    need ^= A[i]
