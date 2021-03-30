import io
import sys

# input here
_INPUT = """\
4 4 8 0

"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque

H, W, A, B = map(int, input().split())

q = deque([])
q.append([0, 0, A, B])
ans = 0
while q:
    i, bit, a, b = q.pop()
    if i == H * W:
        ans += 1
    if bit >> i & 1:
        q.append([i + 1, bit, a, b])
    if b:
        q.append([i + 1, bit | 1 << i, a, b - 1])
    if a:
        if i % W != W - 1 and not bit & 1 << (i + 1):
            q.append([i + 1, bit | 1 << i | 1 << (i + 1), a - 1, b])
        if i + W < H * W:
            q.append([i + 1, bit | 1 << i | 1 << (i + W), a - 1, b])

print(ans)
