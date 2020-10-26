import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

for i in itertools.permutations(range(1, N + 1)):
    num = 0
    for j in range():
