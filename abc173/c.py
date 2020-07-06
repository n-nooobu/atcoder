import numpy as np

H, W, K = input().split(' ')
H = int(H)
W = int(W)
K = int(K)
c = [list(str(input())) for i in range(H)]
cnp = np.array(c)

countAll = np.count_nonzero(cnp == '#')
countH = []
countW = []
for i in range(H):
    countH.append(np.count_nonzero(cnp[i] == '#'))
for i in range(W):
    countW.append(np.count_nonzero(cnp[:, i] == '#'))

ans = 0
for i in range(2 ** H - 1):
    for j in range(2 ** W - 1):
        tmp = countAll
        tmp2 = []
        choiceH = format(i, '0' + str(H) + 'b')
        for m in range(len(choiceH)):
            if int(choiceH[m]):
                tmp -= countH[m]
                tmp2.append(m)
        choiceW = format(j, '0' + str(W) + 'b')
        for n in range(len(choiceW)):
            if int(choiceW[n]):
                tmp -= countW[n]
                for o in range(len(tmp2)):
                    if cnp[tmp2[o], n] == '#':
                        tmp += 1
        if tmp == K:
            ans += 1

print(ans)
