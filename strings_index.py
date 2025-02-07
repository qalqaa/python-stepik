# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')

# s = input()
# for i in range(0, len(s), 2):
#     print(s[i])

# s = input()
# for i in range(len(s) - 1, -1, -1):
#     print(s[i])

# f, i, o = input(), input(), input()
# print(i[0] + f[0] + o[0])

# s = input()
# sm = 0
# for i in range(len(s)):
#     sm += int(s[i])
# print(sm)

# s = input()
# for i in range(len(s)):
#     if s[i] in '0123456789':
#         print('Цифра')
#         break
# else:
#     print('Цифр нет')

# s = input()
# cnt_plus = 0
# cnt_star = 0
# for c in s:
#     if c in '+':
#         cnt_plus += 1
#     elif c in '*':
#         cnt_star += 1
#
# print('Символ + встречается', cnt_plus, 'раз')
# print('Символ * встречается', cnt_star, 'раз')

# s = input()
# cnt = 0
#
# for i in range(len(s)):
#     if i + 1 < len(s):
#         if s[i] == s[i + 1]:
#             cnt += 1
# print(cnt)

# s = input().lower()
# glas_cnt = 0
# sogl_cnt = 0
#
# for c in s:
#     if c in 'ауоыиэяюе':
#         glas_cnt += 1
#     elif c in 'бвгджзйклмнпрстфхцчшщ':
#         sogl_cnt += 1
#
# print('Количество гласных букв равно', glas_cnt)
# print('Количество согласных букв равно', sogl_cnt)

# n = int(input())
#
# print(bin(n)[2:])
