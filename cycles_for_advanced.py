# m, n = int(input()), int(input())
#
# for i in range(m, n + 1):
#     print(i)

# m, n = int(input()), int(input())
#
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# else:
#     for i in range(m, n - 1, -1):
#         print(i)

# m, n = int(input()), int(input())
#
# if m < n:
#     for i in range(m, n + 1, 1):
#         if i % 2 != 0:
#             print(i)
# else:
#     for i in range(m, n - 1, -1):
#         if i % 2 != 0:
#             print(i)

# m, n = int(input()), int(input())
#
# for i in range(m, n + 1):
#     if i % 17 == 0 or i % 10 == 9 or (i % 3 == 0 and i % 5 == 0):
#         print(i)

num = int(input())

for i in range(1, 10 + 1):
    print(num, 'x', i, '=', num * i)
