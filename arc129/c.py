import io
import sys

# input here
_INPUT = """\
2

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

l = [0] * 7
for i in range(7):
    for j in range(1, 10 ** 4):
        tmp = j * (j - 1) // 2
        if tmp > N:
            N -= l[i] * (l[i] - 1) // 2
            break
        l[i] = j
l[6] -= 1

ans = [0] * sum(l)
idx = len(ans) - 1
lidx = 0
ten = 1
num = 0
while idx >= 0:
    for i in range(10):
        if (num + ten * i) % 7 == lidx + 1:
            ans[idx] = i
            ten *= 10
            num = num + ten * i
            idx -= 1
            l[lidx] -= 1
            if l[lidx] == 0:
                lidx += 1

print(*ans, sep='')
