import io
import sys

# input here
_INPUT = """\
1 5
aaaca
"""
sys.stdin = io.StringIO(_INPUT)



H, W = map(int, input().split())
alpha = {chr(ord('a')+i): i for i in range(26)}
count = [0] * 26
for i in range(H):
    a = input()
    for j in a:
        count[alpha[j]] += 1

need = [0] * 3
if H % 2 == 0 and W % 2 == 0:
    need[0] = H // 2 * (W // 2)
elif H % 2 == 0:
    need[0] = H // 2 * (W // 2)
    need[1] = H // 2
elif W % 2 == 0:
    need[0] = H // 2 * (W // 2)
    need[1] = W // 2
else:
    need[0] = H // 2 * (W // 2)
    need[1] = H // 2 + W // 2
    need[2] = 1

for i in range(26):
    if need[0]:
        need[0] -= count[i] // 4
        count[i] %= 4
    if need[1]:
        need[1] -= count[i] // 2
        count[i] %= 2
    if need[2]:
        need[2] -= count[i] % 2
        count[i] -= count[i] % 2

if sum(need) == 0:
    print('Yes')
else:
    print('No')
