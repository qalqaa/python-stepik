# zum_speed = int(input())
# flash_speed = int(input())
# if flash_speed > zum_speed:
#     print('YES')
# elif flash_speed == zum_speed:
#     print("Don't know")
# else:
#     print('NO')

# a, b, c = int(input()), int(input()), int(input())
#
# if a == b == c:
#     print('Равносторонний')
# elif a == b or a == c or b == c:
#     print('Равнобедренный')
# else:
#     print('Разносторонний')


# a, b, c = int(input()), int(input()), int(input())
# array = [a, b, c]
# print(sorted(array)[1])

# month = int(input())
#
# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     print('31')
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     print('30')
# else:
#     print('28')

# weight = int(input())
#
# if weight < 60:
#     print('Легкий вес')
# elif 60 <= weight < 64:
#     print('Первый полусредний вес')
# elif 64 <= weight <= 69:
#     print('Полусредний вес')

# a, b = int(input()), int(input())
# sign = input()
#
# if b == 0 and (sign == '/' or sign == '%'):
#     print('На ноль делить нельзя!')
# elif sign != '/' and sign != '%' and sign != '+' and sign != '-' and sign != '*':
#     print('Неверная операция')
# else:
#     print(eval(f'{a} {sign} {b}'))

# primary_colors = {"красный", "синий", "желтый"}
# color_mixes = {
#     frozenset(["красный", "синий"]): "фиолетовый",
#     frozenset(["красный", "желтый"]): "оранжевый",
#     frozenset(["синий", "желтый"]): "зеленый"
# }
#
# color1, color2 = input(), input()
#
# if color1 in primary_colors and color2 in primary_colors:
#     result = color_mixes.get(frozenset([color1, color2]), color1)
#     print(result)
# else:
#     print("ошибка цвета")

# def get_roulette_color(number: int) -> str:
#     if number == 0:
#         return "зеленый"
#     elif 1 <= number <= 10 or 19 <= number <= 28:
#         return "красный" if number % 2 == 1 else "черный"
#     elif 11 <= number <= 18 or 29 <= number <= 36:
#         return "черный" if number % 2 == 1 else "красный"
#     else:
#         return "ошибка ввода"
#
#
# try:
#     number = int(input())
#     print(get_roulette_color(number))
# except ValueError:
#     print("ошибка ввода")

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

start = max(a1, a2)
end = min(b1, b2)

if start < end:
    print(start, end)
elif start == end:
    print(start)
else:
    print("пустое множество")
