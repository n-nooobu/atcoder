import io
import sys

# input here
_INPUT = """\
4
12 13 1
44 17 17
66 4096 64

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
CSF = [list(map(int, input().split())) for _ in range(N - 1)]

for i in range(N - 1):
    t = CSF[i][1] + CSF[i][0]
    for j in range(i + 1, N - 1):
        if t <= CSF[j][1]:
            t = CSF[j][1] + CSF[j][0]
        else:
            if t % CSF[j][2] == 0:
                t += CSF[j][0]
            else:
                t = (t // CSF[j][2] + 1) * CSF[j][2] + CSF[j][0]

    print(t)
print(0)
