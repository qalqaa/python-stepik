# s = input()
# if s == s.title():
#     print('YES')
# else:
#     print('NO')


# s = input()
# print(s.swapcase())

# s = input()
# if 'хорош' in s.lower():
#     print('YES')
# else:
#     print('NO')

# s = input()
# cnt = 0
# for c in s:
#     if c == c.lower() and not c.isdigit():
#         cnt += 1
# print(cnt)

# s = input()
#
# spaces = s.count(' ')
# if not spaces:
#     print(1)
# else:
#     print(spaces + 1)

# s = input()
#
# print('Аденин:', s.lower().count('а'))
# print('Гуанин:', s.lower().count('г'))
# print('Цитозин:', s.lower().count('ц'))
# print('Тимин:', s.lower().count('т'))

# n = int(input())
# cnt = 0
# for i in range(n):
#     s = input()
#     if s.count('11') >= 3:
#         cnt += 1
# print(cnt)

# s = input()
# cnt = 0
# for i in range(10):
#     cnt += s.count(str(i))
# print(cnt)

# s = input()
# if s.endswith('.com') or s.endswith('.ru'):
#     print('YES')
# else:
#     print('NO')
#
# s = input()
# mx = 0
# st = ''
# for c in s:
#     if mx <= s.count(c):
#         mx = s.count(c)
#         st = c
# print(st)


# s = input()
#
# f_index = s.find('f')
# l_index = s.rfind('f')
# if f_index == l_index and f_index != -1 and l_index != -1:
#     print(f_index)
# elif f_index != -1 and l_index != -1:
#     print(f_index, l_index)
# else:
#     print("NO")

# s = input()
# f_index = s.find('h')
# l_index = s.rfind('h')
# print(s[:f_index] + s[l_index + 1:])

# n = int(input())
# for i in range(n):
#     s = input()
#     if s.isspace() or not s:
#         print(i + 1, ': COMMENT SHOULD BE DELETED', sep='')
#     else:
#         print(i + 1, ': ', s, sep='')


# s = input()
#
# valid_letters = "АВЕКМНОРСТУХ"
# is_valid = False
#
# if (s[0] in valid_letters and
#         s[1:4].isdigit() and
#         s[4] in valid_letters and
#         s[5] in valid_letters and
#         s[6] == '_' and
#         s[7:].isdigit()):
#
#     if len(s[7:]) in (2, 3):
#         is_valid = True
# else:
#     is_valid = False
#
# if is_valid:
#     print('YES')
# else:
#     print('NO')

s = input()

is_valid = False
if s[0] == "@":
    if s[1:].isalnum():
        if s[1:].isdigit():
            if 5 <= len(s) <= 15:
                is_valid = True
        elif s.islower():
            if 5 <= len(s) <= 15:
                is_valid = True
if is_valid:
    print('Correct')
else:
    print('Incorrect')
