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