import io
import sys

# input here
_INPUT = """\
20 15


"""
sys.stdin = io.StringIO(_INPUT)



A, B = map(int, input().split())

print(max(0, A - 2 * B))
