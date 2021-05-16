import io
import sys

# input here
_INPUT = """\
4
QCFium 2846
chokudai 2992
kyoprofriends 2432
penguinman 2390


"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

l = []
for i in range(N):
    s, t = input().split()
    l.append([s, int(t)])

l = sorted(l, key=lambda x: x[1])

print(l[-2][0])
