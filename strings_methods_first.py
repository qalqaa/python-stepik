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

s = input()
cnt = 0
for c in s:
    if c == c.lower() and not c.isdigit():
        cnt += 1
print(cnt)
