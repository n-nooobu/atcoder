import io
import sys

# input here
_INPUT = """\
3
1000000 999999 999998

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))

mod = 10 ** 9 + 7

def prime_factorization(n):
    prime = []
    t = n
    for i in range(2, round(n ** 0.5) + 1):
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

primes = [0] * (max(A) + 1)
prime_list = [[0] * (max(A) + 1) for _ in range(N)]
for i in range(N):
    prime = prime_factorization(A[i])
    for j in range(len(prime)):
        primes[prime[j][0]] = max(primes[prime[j][0]], prime[j][1])
        prime_list[i][prime[j][0]] = prime[j][1]

ans = 0
for i in range(N):
    t = 1
    for j in range(2, len(primes)):
        t = t * pow(j, primes[j] - prime_list[i][j], mod) % mod
    ans = (ans + t) % mod

print(ans)
