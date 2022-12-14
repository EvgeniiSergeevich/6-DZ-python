
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int (input('Введите N: '))
# list = {}
# x = 1
# for i in range(1, n + 1):
#     x *= i
#     list[i - 1] = x
# print(list)



n = int (input('Введите N: '))
list = [i for i in range(n)]
x = 1
for i in range(n):
    x *= (i + 1)
    list[i] = x
print(list)

