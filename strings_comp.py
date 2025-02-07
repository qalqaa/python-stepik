# text = input()
# mx_str = ''
# mn_str = 'я'
# while text.lower() != 'конец':
#     if text > mx_str:
#         mx_str = text
#     if text < mn_str:
#         mn_str = text
#     text = input()
# print('Минимальная строка ⬇️:', mn_str)
# print('Максимальная строка ⬆️:', mx_str)

# mx_str = ''
# mn_str = 'я'
# for _ in range(4):
#     text = input()
#     if text > mx_str:
#         mx_str = text
#     if text < mn_str:
#         mn_str = text
# print((ord(mx_str[-1]) * ord(mn_str[-1])) ** 2)

# n = int(input())
#
# for _ in range(n):
#     is_valid = False
#     s = input()
#     if '0' <= s[0] <= '9':
#         if 'А' < s[1] <= 'П':
#             is_valid = True
#     if is_valid:
#         print('YES')
#     else:
#         print('NO')

# s, s2 = input(), input()
# s_cleared, s2_cleared = '', ''
# for c in s:
#     if c.isalpha():
#         s_cleared += c.lower()
# for c in s2:
#     if c.isalpha():
#         s2_cleared += c.lower()
#
# if s_cleared == s2_cleared:
#     print('YES')
# else:
#     print('NO')

# s, s2, s3 = input(), input(), input()
# mx = max(s, s2, s3)
# mn = min(s, s2, s3)
# md = s + s2 + s3
# md = md.replace(mx, '')
# md = md.replace(mn, '')
# print(mn, md, mx)

# n = int(input())
# is_sorted = True
# prev = ''
# for _ in range(n):
#     s = input()
#     cleared_s = s[0:s.find(' ')] + s[s.find(' ', s.rfind('.')) + 1:]
#     if cleared_s > prev:
#         prev = cleared_s
#     else:
#         is_sorted = False
#         break
# if is_sorted:
#     print('YES')
# else:
#     print('NO')
