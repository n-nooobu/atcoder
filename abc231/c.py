import io
import sys

# input here
_INPUT = """\
5 5
804289384 846930887 681692778 714636916 957747794
424238336
719885387
649760493
596516650
189641422

"""
sys.stdin = io.StringIO(_INPUT)



from bisect import *

N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))

for i in range(Q):
    x = int(input())
    print(N - bisect_left(A, x))
