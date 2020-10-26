import io
import sys

# input here
_INPUT = """\
a

"""
sys.stdin = io.StringIO(_INPUT)



C = input()

print(chr(ord(C) + 1))
