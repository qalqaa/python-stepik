# a, b = int(input()), int(input())
#
# for i in range(a, b + 1):
#     flag = True
#     for j in range(2, i):
#         if i % j == 0:
#             flag = False
#             break
#     if flag and i != 1:
#         print(i)

# n = 4
# count = 0
# maximum = -10 ** 8 + 1
# for _ in range(n):
#     x = int(input())
#     if x % 2 == 0:
#         continue
#     print(x)
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# n = int(input())
# for i in range(n):
#     if i == 0 or i == n - 1:
#         print('*' * 19)
#         continue
#     print('*' + ' ' * 17 + '*')

# n = int(input())
# while n // 1000 > 0:
#     n //= 10
#
# print(n % 10)

# n = int(input())
#
# three_cnt = 0
# last_digit = n % 10
# last_digit_cnt = 0
# even_cnt = 0
# bigger_than_five_sm = 0
# bigger_than_seven_product = 1
# zero_or_five_cnt = 0
#
# while n > 0:
#     if n % 10 == 3:
#         three_cnt += 1
#     if n % 10 == last_digit:
#         last_digit_cnt += 1
#     if n % 10 % 2 == 0:
#         even_cnt += 1
#     if n % 10 > 5:
#         bigger_than_five_sm += n % 10
#     if n % 10 > 7:
#         bigger_than_seven_product *= n % 10
#     if n % 10 == 0 or n % 10 == 5:
#         zero_or_five_cnt += 1
#     n = n // 10
#
# print(three_cnt)
# print(last_digit_cnt)
# print(even_cnt)
# print(bigger_than_five_sm)
# print(bigger_than_seven_product)
# print(zero_or_five_cnt)

ramanujan_numbers = []
n = 1
count = 5
while len(ramanujan_numbers) < count:
    ways = []
    for a in range(1, int(n ** (1 / 3)) + 1):
        b_cubed = n - a ** 3
        if b_cubed > 0:
            b = round(b_cubed ** (1 / 3))
            if a ** 3 + b ** 3 == n and a < b:
                ways.append((a, b))
    if len(ways) >= 2:
        ramanujan_numbers.append(n)
    n += 1
print(ramanujan_numbers)
