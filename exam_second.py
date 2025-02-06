# year = int(input())
# last_digit = year % 10
# prelast_digit = year // 10 % 10
# if last_digit == 0 and prelast_digit == 0:
#     print('YES')
# else:
#     print('NO')

# first_cell_x = int(input())
# first_cell_y = int(input())
# second_cell_x = int(input())
# second_cell_y = int(input())
#
# fist_color = ''
# second_color = ''
#
# if first_cell_x % 2 == 0 and first_cell_y % 2 != 0:
#     fist_color = 'black'
# elif first_cell_x % 2 != 0 and first_cell_y % 2 == 0:
#     fist_color = 'black'
# elif first_cell_x % 2 == 0 and first_cell_y % 2 == 0:
#     fist_color = 'white'
# elif first_cell_x % 2 != 0 and first_cell_y % 2 != 0:
#     fist_color = 'white'
#
# if second_cell_x % 2 == 0 and second_cell_y % 2 != 0:
#     second_color = 'black'
# elif second_cell_x % 2 != 0 and second_cell_y % 2 == 0:
#     second_color = 'black'
# elif second_cell_x % 2 == 0 and second_cell_y % 2 == 0:
#     second_color = 'white'
# elif second_cell_x % 2 != 0 and second_cell_y % 2 != 0:
#     second_color = 'white'
#
# if fist_color == second_color:
#     print('YES')
# else:
#     print('NO')

# age = int(input())
# sex = input()
# if 10 <= age <= 15:
#     if sex == 'f':
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')

# number = int(input())
#
# if 1 <= number <= 10:
#     if number == 1:
#         print('I')
#     elif number == 2:
#         print('II')
#     elif number == 3:
#         print('III')
#     elif number == 4:
#         print('IV')
#     elif number == 5:
#         print('V')
#     elif number == 6:
#         print('VI')
#     elif number == 7:
#         print('VII')
#     elif number == 8:
#         print('VIII')
#     elif number == 9:
#         print('IX')
#     elif number == 10:
#         print('X')
# else:
#     print('ошибка')

# number = int(input())
#
# if number % 2 != 0:
#     print('YES')
# elif 2 <= number <= 5:
#     print('NO')
# elif 6 <= number <= 20:
#     print('YES')
# else:
#     print('NO')

# bishop_position_x, bishop_position_y = int(input()), int(input())
# bishop_target_x, bishop_target_y = int(input()), int(input())
#
# if abs(bishop_position_x - bishop_target_x) == abs(bishop_position_y - bishop_target_y):
#     print('YES')
# else:
#     print('NO')

# knight_position_x, knight_position_y = int(input()), int(input())
# knight_target_x, knight_target_y = int(input()), int(input())
#
# if abs(knight_position_x - knight_target_x) == 2 and abs(knight_position_y - knight_target_y) == 1:
#     print('YES')
# elif abs(knight_position_x - knight_target_x) == 1 and abs(knight_position_y - knight_target_y) == 2:
#     print('YES')
# else:
#     print('NO')

queen_position_x, queen_position_y = int(input()), int(input())
queen_target_x, queen_target_y = int(input()), int(input())

if (queen_position_x == queen_target_x or queen_position_y == queen_target_y) or (
        abs(queen_position_x - queen_target_x) == abs(queen_position_y - queen_target_y)):
    print('YES')
else:
    print('NO')
