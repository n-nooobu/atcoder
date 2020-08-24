import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



H, W, M = map(int, input().split())
hw = []
sh = [0] * H
sw = [0] * W
for i in range(M):
    h, w = map(int, input().split())
    hw.append((h - 1, w - 1))

    sh[h - 1] += 1
    sw[w - 1] += 1

mh = max(sh)
mw = max(sw)

count = 0
for i in range(M):
    if sh[hw[i][0]] == mh and sw[hw[i][1]] == mw:
        count += 1

if sh.count(mh) * sw.count(mw) > count:
    print(mh + mw)
else:
    print(mh + mw - 1)
