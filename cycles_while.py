# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2
#
# print(a)

# text = input()
# while text != 'КОНЕЦ' and text != 'конец':
#     print(text)
#     text = input()


# text = input()
# cnt = 0
#
# while text != 'стоп' and text != 'хватит' and text != 'достаточно':
#     cnt += 1
#     text = input()
#
# print(cnt)

# number = int(input())
# while number % 7 == 0:
#     print(number)
#     number = int(input())

# counter = 0
# number = int(input())
# if number == 5: counter += 1
#
# while 0 < number <= 5:
#     number = int(input())
#     if number == 5: counter += 1
#
# print(counter)

# witchers_order = int(input())
# coins_needed = 0
#
# while witchers_order > 0:
#     if witchers_order >= 25:
#         coins_needed += 1
#         witchers_order -= 25
#     elif witchers_order >= 10:
#         coins_needed += 1
#         witchers_order -= 10
#     elif witchers_order >= 5:
#         coins_needed += 1
#         witchers_order -= 5
#     else:
#         coins_needed += 1
#         witchers_order -= 1
#
# print(coins_needed)

# n = int(input())
# while n > 0:
#     print(n % 10, end='')
#     n = n // 10

# n = int(input())
# mx = 0
# mn = 10
# while n > 0:
#     if n % 10 > mx:
#         mx = n % 10
#     if n % 10 < mn:
#         mn = n % 10
#     n = n // 10
#
# print('Максимальная цифра равна', mx)
# print('Минимальная цифра равна', mn)

# n = int(input())
# sm = 0
# digits_cnt = 0
# digits_product = 1
# digits_average = 0
# first_digit = 0
# last_digit = 0
#
# while n > 0:
#     sm += n % 10
#     digits_cnt += 1
#     digits_product *= n % 10
#     digits_average += n % 10
#     if digits_cnt == 1:
#         last_digit = n % 10
#     if n // 10 <= 0:
#         first_digit = n % 10
#     n = n // 10
#
# print(sm)
# print(digits_cnt)
# print(digits_product)
# print(digits_average / digits_cnt)
# print(first_digit)
# print(first_digit + last_digit)


# n = int(input())
# while n > 0:
#     if n // 100 <= 0 < n // 10:
#         print(n % 10)
#     n = n // 10

# is_same_digits = True
# n = int(input())
# while n > 0:
#     if n % 10 != n // 10 % 10 and n // 10 != 0:
#         is_same_digits = False
#     n = n // 10
# if is_same_digits:
#     print('YES')
# else:
#     print('NO')


n = int(input())
is_lowering = True
while n > 0:
    if (n % 10 > n // 10 % 10) and n // 10 != 0:
        is_lowering = False
    n = n // 10
if is_lowering:
    print('YES')
else:
    print('NO')
