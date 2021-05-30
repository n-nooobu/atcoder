import io
import sys

# input here
_INPUT = """\
7 78314 1055
53515 10620 7271 10000 1910 956 225

"""
sys.stdin = io.StringIO(_INPUT)



K, N, M = map(int, input().split())
A = list(map(int, input().split()))

b = [0] * K
B = [0] * K
s = 0
tura0 = [10 ** 10, 0]
tura1 = [10 ** 10, 0]
for i in range(K):
    b[i] = A[i] * M / N
    B[i] = round(b[i])
    if tura0[0] > A[i] * (B[i] + 1 - b[i]):
        tura0[0] = min(tura0[0], A[i] * (B[i] + 1 - b[i]))
        tura0[1] = i
    if tura1[0] > A[i] * (b[i] - (B[i] - 1)):
        tura1[0] = min(tura1[0], A[i] * (b[i] - (B[i] - 1)))
        tura1[1] = i
    s += B[i]

if s < M:
    B[tura0[1]] += 1
elif s > M:
    B[tura1[1]] -= 1

for i in range(K):
    print(B[i], end=' ')