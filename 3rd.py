# # Напишите программу, которая принимает на вход координаты двух точек и 
# # находит расстояние между ними в 2D пространстве

# xa = int(input('xa = '))
# ya = int(input('ya = '))
# xb = int(input('xb = '))
# yb = int(input('yb = '))

# dist = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
# print(('%.2f' % dist))

import math

xa = int(input('xa = '))
ya = int(input('ya = '))
xb = int(input('xb = '))
yb = int(input('yb = '))

f = lambda b, a: b - a
dist = math.sqrt((f(xb, xa))**2 + (f(yb, ya)) ** 2)

print(('%.2f' % dist))