import io
import sys

# input here
_INPUT = """\
8 1000 800 100
300
333
400
444
500
555
600
666

"""
sys.stdin = io.StringIO(_INPUT)



import itertools

N, A, B, C = map(int, input().split())
l = [int(input()) for _ in range(N)]

ans = 10 ** 9
for i in itertools.product(range(4), repeat=N):
    L = [0] * 4
    mp = 0
    for j in range(len(i)):
        if i[j] < 3 and L[i[j]] > 0:
            mp += 10
        L[i[j]] += l[j]

    mp += abs(L[0] - A) + abs(L[1] - B) + abs(L[2] - C)
    if L[0] and L[1] and L[2]:
        ans = min(ans, mp)

print(ans)
