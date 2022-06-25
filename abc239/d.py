import io
import sys

# input here
_INPUT = """\
3 14 1 5

"""
sys.stdin = io.StringIO(_INPUT)



import sys

A, B, C, D = map(int, input().split())

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

soe = get_sieve_of_eratosthenes(200)

for t in range(A, B + 1):
    flag = True
    for a in range(C, D + 1):
        if t + a in soe:
            flag = False
    if flag:
        print('Takahashi')
        sys.exit()

print('Aoki')
