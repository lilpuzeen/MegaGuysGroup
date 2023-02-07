# Задание 2
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if ((x and y) or (y and z)) == ((x <= w) and (w <= z)):
#                     print(x,y,z,w)
# Ответ:xwzy
# Задание 5
# for n in range(1, 10000):
#     r = bin(n)[2:]
#     r += str(r.count('1') % 2)
#     r += str(r.count('1') % 2)
#     if int(r, 2) > 55:
#         print(int(r, 2))
#         break
# Ответ: 58
# Задание 14
# def calc (x, a, b):
#     s = ''
#     x = int(str(x), a)
#     while x > 0:
#         s += str(x % b)
#         x //= b
#     return s[::-1]
# c = 3*216**4 + 2*36**6 - 648
# result = calc(c, 10, 6)
# print(result.count('5'))
# Ответ: 8
