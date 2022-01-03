import io
import sys

# input here
_INPUT = """\
10
3 1 4 1 5 9 2 6 5 3
2 7 1 8 2 8 1 8 2 8

"""
sys.stdin = io.StringIO(_INPUT)



N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def coordinate_compress(a, duplicate=True):
    if duplicate:
        b = sorted(set(a))
        dic = {v: i for i, v in enumerate(b)}
        return list(map(lambda v: dic[v], a))
    else:
        b = sorted(a)
        dic = {v: i for i, v in enumerate(b)}
        c = []
        for v in a:
            c.append(dic[v])
            dic[v] -= 1
        return c

l = coordinate_compress(B, duplicate=False)
