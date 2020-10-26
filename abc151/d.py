import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



from collections import deque

H, W = map(int, input().split())
S = [input() for _ in range(H)]

def bfs(sh, sw):
    seen = [[False] * W for _ in range(H)]
    q = deque([])
    seen[sh][sw] = True
    q.append([sh, sw])
    while q:
        th, tw = q.popleft
