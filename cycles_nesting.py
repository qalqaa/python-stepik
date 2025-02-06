# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
#
# print(counter)

# n = int(input())
# for i in range(1, n + 1):
#     print(n, n, n)

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(5):
#         print(i, end=' ')
#     print()

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(i, '+', j, '=', i + j)
#     print()

# n = int(input())
#
# for i in range(1, n // 2 + 2):
#     print('*' * i)
#
# for i in range(n // 2, 0, -1):
#     print('*' * i)


# n = int(input())
#
# for i in range(1, n + 1):
#     print(str(i) * i)

# for i in range(1, 100):
#     for j in range(1, 100):
#         for k in range(1, 100):
#             if i * 10 + j * 5 + k * 0.5 == 100:
#                 print(i, j, k)


# limit = 150
# for a in range(1, limit):
#     for b in range(a, limit):
#         for c in range(b, limit):
#             for d in range(c, limit):
#                 sum_powers = a ** 5 + b ** 5 + c ** 5 + d ** 5
#                 e = int(round(sum_powers ** (1 / 5)))
#                 if e ** 5 == sum_powers:
#                     print(a, b, c, d, e)


# n = int(input())
# cnt = 0
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         cnt += 1
#         print(cnt, end=' ')
#     print()

# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end='')
#     for j in range(i - 1, 0, -1):
#         print(j, end='')
#     print()

# max_sm = 0
# max_divider = 0
# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#     sm_divs = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             sm_divs += j
#             if sm_divs >= max_sm:
#                 max_sm = sm_divs
#                 max_divider = i
# print(max_divider, max_sm)

# n = int(input())
#
# for i in range(1, n + 1):
#     print(i, end='')
#     for j in range(1, i + 1):
#         if i % j == 0:
#             print("+", end='')
#     print()

# n = int(input())
#
# while n >= 10:
#     sm = 0
#     while n > 0:
#         sm += n % 10
#         n = n // 10
#     n = sm
# print(n)

# n = int(input())
#
# sm = 0
# for i in range(1, n + 1):
#     fac = 1
#     for j in range(1, i + 1):
#         fac *= j
#     sm += fac
#
# print(sm)

#
