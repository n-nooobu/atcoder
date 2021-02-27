import io
import sys

# input here
_INPUT = """\
31415

"""
sys.stdin = io.StringIO(_INPUT)



K = int(input())

ans = 0
for i in range(1, K + 1):
    for j in range(i, K + 1):
        if i * j > K:
            break
        for k in range(j, K + 1):
            if i * j * k <= K:
                if i == j and j == k:
                    ans += 1
                elif i == j or j == k or k == i:
                    ans += 3
                else:
                    ans += 6
            else:
                break

print(ans)
