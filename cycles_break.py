# n = int(input())
#
# for i in range(2, n + 1):
#     if n % i == 0:
#         print(i)
#         break

n = int(input())

for i in range(1, n + 1):
    if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
        continue
    print(i)
