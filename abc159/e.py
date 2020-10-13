import io
import sys

# input here
_INPUT = """\
4 10 1
1111111111
1111111111
1111111111
1111111111
"""
sys.stdin = io.StringIO(_INPUT)



import itertools

H, W, K = map(int, input().split())
S = [list(input()) for _ in range(H)]

ans = 10 ** 7
for h in itertools.product(range(2), repeat=H-1):
    line = sum(h)
    choco_list = []
    for i in range(W):
        choco_list_ = []
        white = 0
        for j in range(H):
            white += int(S[j][i])
            if (j < H - 1 and h[j]) or j == H - 1:
                choco_list_.append(white)
                white = 0
        choco_list.append(choco_list_)

    continue_flag = False
    for i in range(W):
        for j in range(len(choco_list_)):
            if choco_list[i][j] > K:
                continue_flag = True
    if continue_flag:
        continue

    choco_sum = [0] * len(choco_list_)
    for i in range(W):
        flag = False
        for j in range(len(choco_list_)):
            if choco_sum[j] + choco_list[i][j] > K:
                flag = True
        if flag:
            choco_sum = choco_list[i]
            line += 1
        else:
            for j in range(len(choco_list_)):
                choco_sum[j] += choco_list[i][j]
    ans = min(ans, line)

print(ans)
