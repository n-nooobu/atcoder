import io
import sys

# input here
_INPUT = """\
3
2
2 1
3 0
2
3 1
1 0
2
1 1
2 0

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = []
xy = []
for i in range(N):
    A.append(int(input()))
    xy.append([list(map(int, input().split())) for _ in range(A[i])])

ans = 0
for bit in range(1 << N):
    flag = True
    for i in range(N):
        if bit & 1 << i:
            for x, y in xy[i]:
                if (bit & (1 << (x - 1))) >> (x - 1) != y:
                    flag = False
    if flag:
        ans = max(ans, bin(bit).count('1'))

print(ans)
