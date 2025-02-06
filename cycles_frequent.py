# a, b = int(input()), int(input())
# cnt = 0
# for i in range(a, b + 1):
#     if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
#         cnt += 1
# print(cnt)

# n_amount = int(input())
# sm = 0
# for _ in range(1, n_amount + 1):
#     sm += int(input())
# print(sm)

# from math import *
#
# n = int(input())
# sm = 0
# for i in range(1, n + 1):
#     sm += 1 / i
# print(sm - log(n))

# n = int(input())
# sm = 0
# for i in range(1, n + 1):
#     if i ** 2 % 10 == 2 or i ** 2 % 10 == 5 or i ** 2 % 10 == 8:
#         sm += i
# print(sm)

# n = int(input())
# fac = 1
# for i in range(1, n + 1):
#     fac *= i
# print(fac)

# pr = 1
# for i in range(10):
#     value = int(input())
#     if value != 0:
#         pr *= value
# print(pr)

# n = int(input())
# sm = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         sm += i
# print(sm)

# n = int(input())
# sm = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         sm -= i
#     else:
#         sm += i
# print(sm)

# n = int(input())
# largest = 0
# second_largest = 0
# for i in range(1, n + 1):
#     value = int(input())
#     if value > largest:
#         second_largest = largest
#         largest = value
#     elif value > second_largest:
#         second_largest = value
# print(largest)
# print(second_largest)

# isEven = True
#
# for i in range(1, 11):
#     value = int(input())
#     if value % 2 != 0:
#         isEven = False
#
# if isEven:
#     print('YES')
# else:
#     print('NO')

n = int(input())

fibonacci_list = [0, 1]
for i in range(2, n + 1):
    fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
fibonacci_list.pop(0)
print(' '.join(map(str, fibonacci_list)))
