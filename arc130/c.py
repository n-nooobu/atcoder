import io
import sys

# input here
_INPUT = """\
345
556

"""
sys.stdin = io.StringIO(_INPUT)



from collections import Counter

a = list(input())
b = list(input())

ca = Counter(a)
cb = Counter(b)

ansa = ''
ansb = ''
for key, value in ca.items():
    key2 = 10 - int(key)
    for i in range(key2, 10):
        value2 = cb[str(i)]
        if value > value2:
            ca[key] -= value2
            cb[str(i)] = 0
            ansa += key * value2
            ansb += str(i) * value2
        else:
            ca[key] = 0
            cb[str(i)] -= value
            ansa += key * value
            ansb += str(i) * value
            break

if '9' in ca and ca['9'] > 0:
    ansa += '9' * ca['9']
    ca['9'] = 0
for key, value in ca.items():
    ansa += key * value

if '9' in cb and cb['9'] > 0:
    ansb += '9' * cb['9']
    cb['9'] = 0
for key, value in cb.items():
    ansb += key * value

print(ansa[::-1])
print(ansb[::-1])
