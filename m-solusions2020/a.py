X = int(input())

for i, start in enumerate(range(400, 1900, 200)):
    if start <= X < start + 200:
        print(8 - i)
