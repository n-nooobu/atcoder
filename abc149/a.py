import io
import sys

# input here
_INPUT = """\
oder atc

"""
sys.stdin = io.StringIO(_INPUT)



S, T = input().split()

print(T + S)
