import io
import sys

# input here
_INPUT = """\
54
0 0 1 0 1 2 1 2 3 2 3 3 4 4 5 4 6 5 7 8 5 6 6 7 7 8 8 9 9 10 10 11 9 12 10 13 14 11 11 12 12 13 13 14 14 15 15 15 16 16 16 17 17 17

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7

l = [0, 0, 0]
ans = 1
for i in range(N):
    a = A[i]
    ans *= l.count(a)
    ans %= mod
    for j in range(3):
        if l[j] == a:
            l[j] += 1
            break

print(ans)
