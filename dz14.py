# 19 задача
# def pointinRect(x1 , y1 , x2 , y2 , x3 , y3) :
#     if x1 <= x3 <= x2 and y2 <= y3 <= y1 :
#         return True
#     else :
#         return False
# print(pointinRect(1, 6 , 6 , 1 , 3 , 3))

# задача 20
# Напишите логическую функцию pointInTriangle, которая возвращает значение
# True,	если	точка	с	заданными	координатами	находится	внутри	треугольника,
# заданного координатами трёх своих вершин.

# def side_length(x1, y1, x2, y2):
#     return ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#
# def heron_triangle_area(a, b, c):
#     p = (a + b + c) / 2
#     return (p * (p - a) * (p - b) * (p - c))**0.5
#
# def pointinTriangle(px, py, x1, y1, x2, y2, x3, y3):
#     # Стороны и площадь исходного треугольника ABC
#     a = side_length(x1, y1, x2, y2)
#     b = side_length(x2, y2, x3, y3)
#     c = side_length(x3, y3, x1, y1)
#     area_abc = heron_triangle_area(a, b, c)
#
#     # Стороны и площадь треугольника PAB
#     a1 = side_length(px, py, x1, y1)
#     b1 = side_length(px, py, x2, y2)
#     c1 = side_length(x1, y1, x2, y2)
#     area_pab = heron_triangle_area(a1, b1, c1)
#
#     # Стороны и площадь треугольника PBC
#     a2 = side_length(px, py, x2, y2)
#     b2 = side_length(px, py, x3, y3)
#     c2 = side_length(x2, y2, x3, y3)
#     area_pbc = heron_triangle_area(a2, b2, c2)
#
#     # Стороны и площадь треугольника PCA
#     a3 = side_length(px, py, x3, y3)
#     b3 = side_length(px, py, x1, y1)
#     c3 = side_length(x3, y3, x1, y1)
#     area_pca = heron_triangle_area(a3, b3, c3)
#
#     total_area = area_pab + area_pbc + area_pca
#
#     return round(total_area, 5) == round(area_abc, 5)
#
# print(pointinTriangle(1, 1, 0, 0, 5, 0, 0,5))

# задача 21
# def ocen(a) :
#     a = sorted(a)
#     b = 0
#     for i in range(1, 4) :
#         b += a[i]
#     return b / 3
# a = [35 , 15 , 76 , 66 , 60]
# print("Средняя оценка судей: " , ocen(a))