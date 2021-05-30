import io
import sys

# input here
_INPUT = """\
3
2 3 3
1 3 3
1 1 1


"""
sys.stdin = io.StringIO(_INPUT)



from collections import Counter

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ca = Counter(A)
cb = Counter(B)
cc = Counter(C)

ans = 0
for v, c in cc.items():
    ans += c * ca[B[v - 1]]

print(ans)
