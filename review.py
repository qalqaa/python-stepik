# mx = 0
# s = 0
# for _ in range(11):
#     x = int(input())
#     if x < 0:
#         s += x
#     if x > mx:
#         mx = x
# print(s)
# print(mx)

n = int(input())
while n // 10 > 0:
    n = n // 10
print(n)
