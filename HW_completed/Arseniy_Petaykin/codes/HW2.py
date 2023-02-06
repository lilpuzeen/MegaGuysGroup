# # Задание 2 (№14688)
# print('x y z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if not((x or y) <= (z == x)):
#                 print(x,y,z)
# Ответ:xzy

# # Задание 2 (№15097)
# print('x y z')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             if not((x == z) or (x <= y and z)):
#                 print(x,y,z)
# Ответ:yzx

# # Задание 2 (№15814)
# print('x y z w')
# for x in range(2):
#     for y in range(2):
#         for z  in range(2):
#             for w in range(2):
#                 if not((x == (w or y)) or ((w <= z) and (y <= w))):
#                     print(x,y,z,w)
# Ответ:yxzw

# # Задание 5 (№27535)

# for n in range(4, 1000):
#     r = bin(n)[2:]
#     r = r + r[1] + r[0]
#     print(int(r, 2), n)

# Ответ:23