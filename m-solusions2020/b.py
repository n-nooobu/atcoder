import sys

A, B, C = map(int, input().split())
K = int(input())

for a in range(K):
    for b in range(K):
        if A * 2**a < B * 2**b < C * 2**(K-(a+b)):
            print('Yes')
            sys.exit()

print('No')
