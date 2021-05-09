import io
import sys

# input here
_INPUT = """\
1000000 1000000000000000000


"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())

c = [0] * (3 * N + 1)
mid = (3 + 3 * N) // 2
for i, k in enumerate(range(3, mid)):
    c[k] = c[k - 1] + (i + 1)
    c[3 * N - i] = c[k]
if N == 2:
    c[mid] = c[mid - 1] + N
else:
    c[mid] = c[mid - 1] + N - 2
if not c[mid + 1]:
    c[mid + 1] = c[mid]
for i in range(1, len(c)):
    c[i] += c[i - 1]
    if c[i] >= K:
        s = i
        K -= c[i - 1]
        break

c2 = [0] * (2 * N + 1)
mid2 = (2 + 2 * N) // 2
for i, k in enumerate(range(2, mid2)):
    c2[k] = i + 1
    c2[2 * N - i] = c2[k]
c2[mid2] = N

t = 0
for i, k in enumerate(range(s - 1, 0, -1)):
    if t + c2[k] >= K:
        first = i + 1
        K -= t
        break
    t += c2[k]

count = 0
for i in range(1, N + 1):
    if s - first - i <= N:
        count += 1
    if count == K:
        print(first, i, s - first - i)
        break
