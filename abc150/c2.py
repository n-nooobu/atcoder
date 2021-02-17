import io
import sys

# input here
_INPUT = """\
3
1 2 3
1 2 3

"""
sys.stdin = io.StringIO(_INPUT)



import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

k = 0
for i in itertools.permutations([i for i in range(1, N + 1)]):
    k += 1
    flag_p = True
    flag_q = True
    for j in range(len(i)):
        if P[j] != i[j]:
            flag_p = False
        if Q[j] != i[j]:
            flag_q = False
    if flag_p:
        p = k
    if flag_q:
        q = k

print(abs(p - q))
