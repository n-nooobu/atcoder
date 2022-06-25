import io
import sys

# input here
_INPUT = """\
7
4 8 1 7 9 5 6
3 5 1 7 8 2 6

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans0, ans1 = 0, 0
for i in range(N):
    for j in range(N):
        if A[i] == B[j]:
            if i == j:
                ans0 += 1
            else:
                ans1 += 1

print(ans0)
print(ans1)
