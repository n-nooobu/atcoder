import io
import sys

# input here
_INPUT = """\
999

"""
sys.stdin = io.StringIO(_INPUT)



L = int(input())

print((L / 3) ** 3)
