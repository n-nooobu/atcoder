import io
import sys

# input here
_INPUT = """\
2 5


"""
sys.stdin = io.StringIO(_INPUT)



N, K = map(int, input().split())

c = [0] * (3 * N + 1)

