# n = int(input())
# arr = list()
# for i in range(ord('a'), ord('a') + n):
#     arr.append(chr(i))
# print(arr)
# # print(range(ord('a') + 1, ord('z') + 1))

# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
#
# print(primes[:6])

arr = []
for i in range(1, 27):
    arr.append(chr(ord('a') - 1 + i) * i)
print(arr)
