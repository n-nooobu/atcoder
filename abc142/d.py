import io
import sys

# input here
_INPUT = """\
1 2019


"""
sys.stdin = io.StringIO(_INPUT)



import math

A, B = map(int, input().split())

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

G = math.gcd(A, B)
prime = prime_factorization(G)

print(len(prime) + 1)
