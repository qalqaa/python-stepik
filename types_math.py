from math import *

# x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
#
# print(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

# radius = float(input())
# print(pi * radius ** 2)
# print(2 * pi * radius)


# a, b = float(input()), float(input())
#
# print((a + b) / 2)
# print(sqrt(a * b))
# print((2 * a * b) / (a + b))
# print(sqrt((a ** 2 + b ** 2) / 2))

# x = float(input())
#
# r = x * pi / 180
# print(sin(r) + cos(r) + (tan(r) ** 2))

# x = float(input())
# print(floor(x) + ceil(x))

# a, b, c = float(input()), float(input()), float(input())
#
# D = b ** 2 - 4 * a * c
# if D < 0:
#     print('Нет корней')
# elif D == 0:
#     x = -b / (2 * a)
#     print(x)
# else:
#     x1 = (-b + sqrt(D)) / (2 * a)
#     x2 = (-b - sqrt(D)) / (2 * a)
#     print(min(x1, x2))
#     print(max(x1, x2))

n, a = float(input()), float(input())
print((n * a ** 2) / (4 * tan(pi / n)))
