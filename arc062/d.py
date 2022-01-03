import io
import sys

# input here
_INPUT = """\
ggppgggpgg

"""
sys.stdin = io.StringIO(_INPUT)



s = input()

print(s[1::2].count('g') - s[::2].count('p'))
