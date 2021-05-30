import io
import sys

# input here
_INPUT = """\
14
630551244 683685976 249199599 863395255 667330388 617766025 564631293 614195656 944865979 277535591 390222868 527065404 136842536 971731491

"""
sys.stdin = io.StringIO(_INPUT)



from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cum = [0]
for i in range(N):
    if i % 2:
        cum.append(cum[-1] - A[i])
    else:
        cum.append(cum[-1] + A[i])

c = Counter(cum)
ans = 0
for i in range(N):
    ans += c[cum[i]] - 1
    c[cum[i]] -= 1

print(ans)
