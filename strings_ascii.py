# print(ord('a'))
# print(ord('A'))
# print(ord('z'))
# print(ord('Z'))
# print(ord('6'))
# print(ord('7'))

# c = input()
# if (c != 'я') and (c != 'Я'):
#     print(chr(ord(c) + 1))
# else:
#     print('Дальше букв нет')

# a, b = int(input()), int(input())
#
# for i in range(a, b + 1):
#     print(chr(i), end=' ')

# s = input()
# for i in range(len(s)):
#     print(ord(s[i]), end=' ')

# a, b, c, d = input(), input(), input(), input()
# sma, smb, smc, smd = 0, 0, 0, 0
#
# for n in a:
#     sma += ord(n)
# for n in b:
#     smb += ord(n)
# for n in c:
#     smc += ord(n)
# for n in d:
#     smd += ord(n)
# smax = max(sma, smb, smc, smd)
#
# if smax == sma:
#     print(a)
# elif smax == smb:
#     print(b)
# elif smax == smc:
#     print(c)
# else:
#     print(d)

# s = input()
# eng = "eyopaxcETOPAHXCBM"
# rus = "еуорахсЕТОРАНХСВМ"
# old = s
# sm = 0
# old_sm = 0
#
# for i in range(len(eng)):
#     s = s.replace(eng[i], rus[i])
# for c in old:
#     old_sm += ord(c)
# for c in s:
#     sm += ord(c)
# print(f'Старая стоимость: {old_sm * 3}🐝')
# print(f'Новая стоимость: {sm * 3}🐝')

# n, s = int(input()), input()
#
# for c in s:
#     print(chr((ord(c) - ord('a') - n) % 26 + ord('a')), end='')


n = input()
result = ""
i = 0
while i < len(n):
    if n[i:i + 3] == "[u-":
        j = i + 3
        while j < len(n) and n[j].isdigit():
            j += 1
        if j < len(n) and n[j] == ']':
            unicode_number = int(n[i + 3:j])
            result += chr(unicode_number)
            i = j + 1
            continue
    result += n[i]
    i += 1
print(result)
