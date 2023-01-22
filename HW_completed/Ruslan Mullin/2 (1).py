# '''#1 задание
# print('x y z')
# for x in range (0,2):
#     for y in range (0,2):
#         for z in range (0,2):
#             if ((x or y) <= (z == x)) == 0:
#                 print(x, y, z)
# #Ответ: xzy '''
#
# '''#2 задание
# print('x y z')
# for x in range (0,2):
#     for y in range (0,2):
#         for z in range (0,2):
#             if (x == y) or (x <= (y or z)) == 0:
#                 print(x, y, z)
# #Ответ: yzw '''
#
#3 задание
# print('x y z w')
# for x in range (0,2):
#     for y in range (0,2):
#         for z in range (0,2):
#             for w in range(0, 2):
#                 if (x == (w or y)) or ((w <= z) and (y <= w)):
#                     print(x, y, z)
# #Ответ: yxzw
#
# for i in range(2, 1000):
#     n = bin(i)[2:]
#     n = n + n[0] + n[1]
#     n = int(n, 2)
#     if n > 90:
#         print(n)