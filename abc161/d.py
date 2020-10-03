import io
import sys

# input here
_INPUT = """\
100000
"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque

K = int(input())

d = deque(range(1, 10))
for _ in range(K):
    num = d.popleft()
    if num % 10 != 0:
        d.append(num * 10 + (num % 10 - 1))
    d.append(num * 10 + num % 10)
    if num % 10 != 9:
        d.append(num * 10 + num % 10 + 1)

print(num)
