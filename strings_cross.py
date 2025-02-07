# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::-1])

# s = input()
# if s[::-1] == s:
#     print('YES')
# else:
#     print('NO')

# s = input()
# print(len(s))
# print(s * 3)
# print(s[0])
# print(s[:3])
# print(s[-3:])
# print(s[::-1])
# print(s[1:-1])

# s = input()
#
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[::-2])

s = input()
if (len(s) % 2) != 0:
    print(s[len(s) // 2 + 1:])
    print(s[:len(s) // 2 + 1], end='')
else:
    print(s[len(s) // 2:], end='')
    print(s[:len(s) // 2])
