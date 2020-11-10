import io
import sys

# input here
_INPUT = """\

"""
sys.stdin = io.StringIO(_INPUT)



A, B = map(int, input().split())

print(max(0, 2 * A + 100 - B))

