import io
import sys

# input here
_INPUT = """\
100

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

def prime_factorization(n):
    prime = []
    t = n
    for i in range(2, int(n ** 0.5) + 1):
        if t % i != 0:
            continue
        count = 0
        while t % i == 0:
            count += 1
            t //= i
        prime.append([i, count])
    if t != 1:
        prime.append([t, 1])
    return prime

insuu = [0] * (N + 1)
for i in range(2, N + 1):
    prime = prime_factorization(i)
    for num, cnt in prime:
        insuu[num] += cnt

count = [0] * 5
for i in insuu:
    if i >= 2:
        count[0] += 1
    if i >= 4:
        count[1] += 1
    if i >= 14:
        count[2] += 1
    if i >= 24:
        count[3] += 1
    if i >= 74:
        count[4] += 1

print(count[4] + count[3] * (count[0] - 1) + count[2] * (count[1] - 1)
      + count[1] * (count[1] - 1) // 2 * (count[0] - 2))
