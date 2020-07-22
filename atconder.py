from collections import Counter

n, m = map(int, input().split())
ka = []
for i in range(n):
    x = [int(y) for y in input().split()]
    ka.extend(x[1:])

count = 0
for i,j in Counter(ka).items():
    if j == n:
        count += 1
print(count)

