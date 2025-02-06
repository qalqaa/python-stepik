# first_pass, second_pass = input(), input()
# if first_pass == second_pass:
#     print('Пароль принят')
# else:
#     print('Пароль не принят')
# number = int(input())
# if number % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')


# number = int(input())
#
# first_digit, second_digit, third_digit, fourth_digit = number // 1000, number // 100 % 10, number // 10 % 10, number % 10
#
# if (first_digit + fourth_digit) == (second_digit - third_digit):
#     print('ДА')
# else:
#     print('НЕТ')


# user_age = int(input())
#
# if user_age >= 18:
#     print('Доступ разрешен')
# else:
#     print('Доступ запрещен')


# x, y, z = int(input()), int(input()), int(input())
#
# if x - y == y - z:
#     print('YES')
# else:
#     print('NO')


# first_number, second_number = int(input()), int(input())
#
# if first_number < second_number:
#     print(first_number)
# else:
#     print(second_number)

# first_number, second_number, third_number, fourth_number = int(input()), int(input()), int(input()), int(input())
#
# min_number = first_number
#
# if second_number < min_number:
#     min_number = second_number
# if third_number < min_number:
#     min_number = third_number
# if fourth_number < min_number:
#     min_number = fourth_number
#
# print(min_number)

# age = int(input())
# if age <= 13:
#     print('детство')
# elif 14 <= age <= 24:
#     print('молодость')
# elif 25 <= age <= 59:
#     print('зрелость')
# else:
#     print('старость')
a, b, c = int(input()), int(input()), int(input())

positive_sum = 0

if a > 0:
    positive_sum += a
if b > 0:
    positive_sum += b
if c > 0:
    positive_sum += c

print(positive_sum)
