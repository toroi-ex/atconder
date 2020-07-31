# from collections import Counter

# n, m = map(int, input().split())
# ka = []
# for i in range(n):
#     x = [int(y) for y in input().split()]
#     ka.extend(x[1:])

# count = 0
# for i,j in Counter(ka).items():
#     if j == n:
#         count += 1
# print(count)

#121 A
# H, W = map(int, input().split())
# h, w = map(int, input().split())

# print((H-h)*(W-w))

#121 B
# from operator import mul
# n, m, c = map(int, input().split())
# b = list(map(int, input().split()))
# count = 0

# for i in range(n):
#     a = list(map(int, input().split()))
#     com = map(mul, a, b)
#     if sum(com) + c > 0:
#         count += 1
#     a.clear()

# print(count)

#121 C
# n, m = map(int, input().split())
# ab = []
# for i in range(n):
#     AB = list(map(int, input().split()))
#     ab.append(AB)
# x = 0
# val = 0
# ab.sort(key=lambda x:x[0])
# for i in range(n):
#     x += ab[i][1]
#     val += ab[i][0]*ab[i][1]
#     if x < m:
#         continue
#     else:
#         val = val - ab[i][0]*(x - m)
#         break
# print(val)