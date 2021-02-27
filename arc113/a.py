import io
import sys

# input here
_INPUT = """\
200000
"""
sys.stdin = io.StringIO(_INPUT)



K = int(input())

ans = 0
for k in range(1, K + 1):
    divisor = []
    for i in range(1, int(k ** 0.5) + 1):
        if k % i == 0:
            divisor.append(i)
            if k // i != i:
                divisor.append(k // i)
    for i in range(len(divisor)):
        n = k // divisor[i]
        divisor2 = []
        for j in range(1, int(n ** 0.5) + 1):
            if n % j == 0:
                divisor2.append(j)
                if n // j != j:
                    divisor2.append(n // j)
        ans += len(divisor2)

print(ans)
