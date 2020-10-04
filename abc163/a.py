import io
import sys

# input here
_INPUT = """\
14282668646
"""
sys.stdin = io.StringIO(_INPUT)



import numpy as np

R = int(input())

print(2 * np.pi * R)
