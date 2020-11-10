import io
import sys

# input here
_INPUT = """\
15 10
554 525 541 814 661 279 668 360 382 175 833 783 688 793 736
496 732 455 306 189 207 976 73 567 759

"""
sys.stdin = io.StringIO(_INPUT)



N, M = map(int, input().split())
H = sorted(list(map(int, input().split())))
W = sorted(list(map(int, input().split())))

first_cost = 0
for i in range(1, N, 2):
    first_cost += H[i + 1] - H[i]

pair_costs = [0] * (N // 2 + 1)
pair_costs[0] = first_cost
for i in range(1, N // 2 + 1):
    pair_costs[i] = pair_costs[i - 1] - (H[i * 2] - H[i * 2 - 1]) + (H[(i - 1) * 2 + 1] - H[(i - 1) * 2])

ans = 10 ** 18
now_id = 0
for i in range(len(pair_costs)):
    for j in range(now_id, M):
        if W[j] < H[i * 2]:
            ans = min(ans, pair_costs[i] + abs(W[j] - H[i * 2]))
            now_id = j
        elif W[j] == H[i * 2]:
            ans = min(ans, pair_costs[i])
            break
        else:
            ans = min(ans, pair_costs[i] + abs(W[j] - H[i * 2]))

print(ans)
