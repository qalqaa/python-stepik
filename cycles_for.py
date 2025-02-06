# for i in range(10):
#     print('Python is awesome!')

# for i in range(6):
#     print('AAA')
# for i in range(5):
#     print('BBBB')
# print('E')
# for i in range(9):
#     print('TTTTT')
# print('G')

# string, iterations = input(), int(input())
#
# for i in range(iterations):
#     print(string)
#
# height = int(input())
# for i in range(height):
#     print('*' * 19)

# string = input()
# for i in range(10):
#     print(i, string)

# iterations = int(input())
# for i in range(iterations + 1):
#     print('Квадрат числа', i, 'равен', i ** 2)

# height = int(input())
# for i in range(height):
#     print('*' * (height - i))

m, p, n = int(input()), int(input()), int(input())
population = m
for i in range(1, n + 1):
    print(i, population)
    population = population + (population * (p / 100))
