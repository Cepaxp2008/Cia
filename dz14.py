# 19 задача
# def pointinRect(x1 , y1 , x2 , y2 , x3 , y3) :
#     if x1 <= x3 <= x2 and y2 <= y3 <= y1 :
#         return True
#     else :
#         return False
# print(pointinRect(1, 6 , 6 , 1 , 3 , 3))

# задача 20 неправильно

# def pointInTriangle (x0 , y0 , x1 , y1 , x2 , y2 , x3 , y3) :
#     if ((x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0) > 0)
#         and ((x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0) > 0)
#              and ((x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0) > 0)
#         or ((((x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0) < 0)
#              and ((x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0) < 0)
#             and ((x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0) < 0))
#             or ((x1 - x0) * (y2 - y1) - (x2 - x1) * (y1 - y0) == 0))
#              or ((x2 - x0) * (y3 - y2) - (x3 - x2) * (y2 - y0) == 0)
#         or ((x3 - x0) * (y1 - y3) - (x1 - x3) * (y3 - y0) == 0) :
#         return True
#     else :
#         return False
# print(pointInTriangle( 0, 0 , 0 , 0 , 0 , 5 , 5, 0))

# задача 21
# def ocen(a) :
#     a = sorted(a)
#     b = 0
#     for i in range(1, 4) :
#         b += a[i]
#     return b / 3
# a = [35 , 15 , 76 , 66 , 60]
# print("Средняя оценка судей: " , ocen(a))