N = int(input())

for i in range(12):
    if i * 1000 >= N:
        print(i * 1000 - N)
        break
