import io
import sys

# input here
_INPUT = """\
7
5 0 7 8 3 3 2


"""
sys.stdin = io.StringIO(_INPUT)



import itertools

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in itertools.combinations(range(N), 2):
    ans += A[i[0]] * A[i[1]]

print(ans)
