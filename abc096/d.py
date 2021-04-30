import io
import sys

# input here
_INPUT = """\
5
"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

def get_sieve_of_eratosthenes(n):
    prime = [2]
    limit = int(n ** 0.5)
    data = [i for i in range(3, n + 1, 2)]
    while True:
        p = data[0]
        if limit < p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

sieve = get_sieve_of_eratosthenes(55555)
ans = []
for p in sieve:
    if p % 5 == 1:
        ans.append(p)

for i in range(N):
    print(ans[i], end=' ')
