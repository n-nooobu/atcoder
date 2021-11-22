import io
import sys

# input here
_INPUT = """\
1000000000000000000 1 1000000000000000000

"""
sys.stdin = io.StringIO(_INPUT)



N, L, R= map(int, input().split())

ans = 0
Nb = bin(N)[2:]
for i in range(len(Nb)):
    if Nb[i] == '1':
        M = min(R, pow(2, len(Nb) - i) - 1)
        m = max(L, pow(2, len(Nb) - 1 - i))
        if M >= m:
            ans += M - m + 1

print(ans)
