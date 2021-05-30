import io
import sys

# input here
_INPUT = """\
4

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

sieve = get_sieve_of_eratosthenes(10 ** 4 + 1)
print(6, 10, 15, end=' ')
a = []
six = 2
while 6 * six <= 10 ** 4:
    a.append(6 * six)
    six += 1
ten = 2
while 10 * ten <= 10 ** 4:
    if 10 * ten % 3:
        a.append(10 * ten)
    ten += 1
fifteen = 2
while 15 * fifteen <= 10 ** 4:
    if 15 * fifteen % 2:
        a.append(15 * fifteen)
    fifteen += 1
k = 0
while k < N - 3:
    print(a[k], end=' ')
    k += 1
