# a, b = float(input()), float(input())
#
# print(0.5 * a * b)

# s, v1, v2 = float(input()), float(input()), float(input())
#
# print(s / (v1 + v2))

# num = float(input())
# if num != 0:
#     print(1 / num)
# else:
#     print('Обратного числа не существует')

# t_farengait = float(input())
# print((t_farengait - 32) * 5 / 9)

# dog_age = float(input())
# if dog_age <= 2:
#     print(dog_age * 10.5)
# else:
#     print(21 + (dog_age - 2) * 4)

# float_input = float(input())
# print(int(float_input % 1 * 10))

# float_input = float(input())
# print(float_input % 1)

# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
# print('Наименьшее число =', min(a, b, c, d, e))
# print('Наибольшее число =', max(a, b, c, d, e))

# a, b, c = int(input()), int(input()), int(input())
# print(max(a, b, c))
# print(a + b + c - max(a, b, c) - min(a, b, c))
# print(min(a, b, c))

# number = int(input())
# first_digit, second_digit, third_digit = number // 100 % 10, number // 10 % 10, number % 10
# max_digit = max(first_digit, second_digit, third_digit)
# min_digit = min(first_digit, second_digit, third_digit)
#
# if max_digit - min_digit == (first_digit + second_digit + third_digit - max_digit - min_digit):
#     print('Число интересное')
# else:
#     print('Число неинтересное')

# a, b, c, d, e = float(input()), float(input()), float(input()), float(input()), float(input())
#
# print(abs(a) + abs(b) + abs(c) + abs(d) + abs(e))

p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
print(abs(p1 - q1) + abs(p2 - q2))
