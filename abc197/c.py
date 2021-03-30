import io
import sys

# input here
_INPUT = """\
4
1 3 3 1

"""
sys.stdin = io.StringIO(_INPUT)



import itertools

N = int(input())
A = list(map(int, input().split()))

ans = 10 ** 11
for i in itertools.product(range(2), repeat=N-1):
    OR = A[0]
    XOR = 0
    for j in range(len(i)):
        if i[j]:
            OR = OR | A[j+1]
        else:
            XOR = XOR ^ OR
            OR = A[j+1]
    XOR = XOR ^ OR
    ans = min(ans, XOR)

print(ans)
