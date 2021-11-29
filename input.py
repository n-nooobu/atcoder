import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())

A = list(map(int, input().split()))

H, W, M = map(int, input().split())

c = [input() for _ in range(H)]
# ['s####', '....#', '#####', '#...g']
# 文字を変えられない
c = [list(input()) for _ in range(H)]
# [['s', '#', '#', '#', '#'], ['.', '.', '.', '.', '#'], ['#', '#', '#', '#', '#'], ['#', '.', '.', '.', 'g']]
# 文字を変えられる

rcv = [list(map(int, input().split())) for _ in range(N)]
# [[1, 1, 3], [2, 1, 4], [1, 2, 5]]


from collections import defaultdict

G = defaultdict(set)
for idx in range(N):
    A = AB[idx][0] - 1
    B = AB[idx][1] - 1
    G[A].add(B)
    G[B].add(A)
