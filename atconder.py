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

#123 B
# a = []
# b = [0]
# ans = 0

# for i in range(5):
#     A = int(input())
#     B = A % 10
#     if B != 0:
#         A = A + (10 - B)
#         b.append(B)
#     a.append(A)
# if sorted(set(b))[1] != 0:
#     ans = sum(a) - (10 - sorted(set(b))[1])
# else:
#     ans = sum(a)

# print(ans)

#123 C
# import math
# n = int(input())
# a = [int(input()) for _ in range(5)]
# print(4+math.ceil(n / min(a)))

#125 A
# n, k = map(int, input().split())
# S = input()

# s = S[:k-1] + S[k-1].lower() + S[k:]
# print(s)

#125 B
# s = input()
# s1 = int(s[0:2])
# s2 = int(s[2:])

# if s1 > 0 and s1 < 13:
#     if s2 > 0 and s2 < 13:
#         print("AMBIGUOUS")
#     else:
#         print("MMYY")
# else:
#     if s2 > 0 and s2 < 13:
#         print("YYMM")
#     else:
#         print("NA")

#125 C
# n, k = map(int, input().split())
# ans = 0
# for i in range(1,n + 1):
#     a = 0
#     while i < k:
#         i *= 2
#         a += 1
#     ans += 1/n * (1/2)**a
# print(ans)