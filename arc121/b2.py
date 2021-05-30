import io
import sys

# input here
_INPUT = """\
1
1 R
2 G


"""
sys.stdin = io.StringIO(_INPUT)



from bisect import *

N = int(input())

color = {'R': 0, 'G': 1, 'B': 2}
kawaisa = [[] for _ in range(3)]
for i in range(2 * N):
    a, c = input().split()
    kawaisa[color[c]].append(int(a))
length = [0, 0, 0]
for i in range(3):
    kawaisa[i] = sorted(kawaisa[i])
    length[i] = len(kawaisa[i])

if length[0] % 2 == 0 and length[1] % 2 == 0 and length[2] % 2 == 0:
    print(0)
else:
    if length[0] % 2 == 0:
        tar0, tar1, tar2 = 1, 2, 0
    elif length[1] % 2 == 0:
        tar0, tar1, tar2 = 0, 2, 1
    elif length[2] % 2 == 0:
        tar0, tar1, tar2 = 0, 1, 2

    mi1, mi2, mi3 = 10 ** 17, 10 ** 17, 10 ** 17

    l = kawaisa[tar1]
    for a in kawaisa[tar0]:
        if 0 < bisect_left(l, a) < length[tar1]:
            t = min(abs(a - l[bisect_left(l, a)]), abs(a - l[bisect_left(l, a) - 1]))
        elif bisect_left(l, a) == 0:
            t = abs(a - l[bisect_left(l, a)])
        else:
            t = abs(a - l[bisect_left(l, a) - 1])
        mi1 = min(mi1, t)

    l = kawaisa[tar2]
    for a in kawaisa[tar0]:
        if kawaisa[tar2]:
            if 0 < bisect_left(l, a) < length[tar2]:
                t = abs(a - l[bisect_left(l, a)])
                if t < mi2:
                    mi2 = t
                    mi2_idx = bisect_left(l, a)
                t = abs(a - l[bisect_left(l, a) - 1])
                if t < mi2:
                    mi2 = t
                    mi2_idx = bisect_left(l, a) - 1
            elif bisect_left(l, a) == 0:
                t = abs(a - l[bisect_left(l, a)])
                if t < mi2:
                    mi2 = t
                    mi2_idx = bisect_left(l, a)
            else:
                t = abs(a - l[bisect_left(l, a) - 1])
                if t < mi2:
                    mi2 = t
                    mi2_idx = bisect_left(l, a) - 1
    for a in kawaisa[tar1]:
        if kawaisa[tar2]:
            if 0 < bisect_left(l, a) < length[tar2]:
                t = abs(a - l[bisect_left(l, a)])
                if t < mi3 and bisect_left(l, a) != mi2_idx:
                    mi3 = t
                t = abs(a - l[bisect_left(l, a) - 1])
                if t < mi3 and bisect_left(l, a) - 1 != mi2_idx:
                    mi3 = t
            elif bisect_left(l, a) == 0:
                t = abs(a - l[bisect_left(l, a)])
                if t < mi3 and bisect_left(l, a) != mi2_idx:
                    mi3 = t
            else:
                t = abs(a - l[bisect_left(l, a) - 1])
                if t < mi3 and bisect_left(l, a) - 1 != mi2_idx:
                    mi3 = t

    print(min(mi1, mi2 + mi3))
