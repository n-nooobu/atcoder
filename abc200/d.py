import io
import sys

# input here
_INPUT = """\
6
2013 1012 2765 2021 508 6971



"""
sys.stdin = io.StringIO(_INPUT)



import itertools

N = int(input())
A = list(map(int, input().split()))

a = [0] * N
for i in range(N):
    a[i] = A[i] % 200

amari = [[] for _ in range(200)]
for i in itertools.product(range(2), repeat=N):
    l = []
    t = 0
    for j in range(len(i)):
        if i[j]:
            l.append(j + 1)
            t += a[j]
    t %= 200
    if amari[t]:
        print('Yes')
        print(*([len(amari[t])] + amari[t]), sep=' ')
        print(*([len(l)] + l), sep=' ')
        exit()
    else:
        amari[t] = l

print('No')
