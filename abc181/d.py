import io
import sys

# input here
_INPUT = """\
62

"""
sys.stdin = io.StringIO(_INPUT)



import sys

S = input()

if len(S) == 1:
    if int(S) % 8 == 0:
        print('Yes')
    else:
        print('No')
elif len(S) == 2:
    if int(S) % 8 == 0 or int(S[1] + S[0]) % 8 == 0:
        print('Yes')
    else:
        print('No')
else:
    eights = []
    for i in range(1000):
        if i % 8 == 0:
            t = []
            for j in range(3):
                t.append(i % 10)
                i //= 10
            eights.append(t)
    l = [0] * 10
    for i in range(len(S)):
        l[int(S[i])] += 1
    for i in range(len(eights)):
        l2 = [0] * 10
        for j in range(3):
            l2[eights[i][j]] += 1
        flag = True
        for j in range(10):
            if l[j] < l2[j]:
                flag = False
        if flag:
            print('Yes')
            sys.exit()

    print('No')
