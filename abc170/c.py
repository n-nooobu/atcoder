XN = list(map(int, input().split(' ')))
if XN[1] == 0:
    print(XN[0])
else:
    p = list(map(int, input().split(' ')))
    count = [0] * 110
    for i in range(XN[1]):
        count[p[i] + 5] += 1
    for i in range(60):
        if count[XN[0] + 5 - i] == 0:
            print(XN[0] - i)
            break
        elif count[XN[0] + 5 + i] == 0:
            print(XN[0] + i)
            break
