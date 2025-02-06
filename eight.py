# number = int(input())
# numbers_sum = 0
# numbers_product = 1
#
# while number > 0:
#     numbers_sum += number % 10
#     numbers_product *= number % 10
#     number = number // 10
#
# print('Сумма цифр =', numbers_sum)
# print('Произведение цифр =', numbers_product)


# number = int(input())
# third_digit = number % 10
# second_digit = number // 10 % 10
# first_digit = number // 100 % 10
#
# print(first_digit, second_digit, third_digit, sep='')
# print(first_digit, third_digit, second_digit, sep='')
# print(second_digit, first_digit, third_digit, sep='')
# print(second_digit, third_digit, first_digit, sep='')
# print(third_digit, first_digit, second_digit, sep='')
# print(third_digit, second_digit, first_digit, sep='')
# # for i in range(6):
# #     print(first_digit, second_digit, third_digit, sep='')
# #     first_digit, second_digit, third_digit = second_digit, third_digit, first_digit


# Цифра в позиции тысяч равна 3
# Цифра в позиции сотен равна 2
# Цифра в позиции десятков равна 8
# Цифра в позиции единиц равна 1
number = int(input())
numbers_array = [number % 10, number // 10 % 10, number // 100 % 10, number // 1000 % 10]

print('Цифра в позиции тысяч равна', numbers_array[3])
print('Цифра в позиции сотен равна', numbers_array[2])
print('Цифра в позиции десятков равна', numbers_array[1])
print('Цифра в позиции единиц равна', numbers_array[0])
