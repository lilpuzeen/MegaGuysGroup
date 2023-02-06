# 2
# https://dropmefiles.com/8GN3M
# print('x y z w F')
# for x in range(2):
#     for y in range(2):
#         for z in range(2):
#             for w in range(2):
#                 if (((x and y) or (y and z)) == ((x <= w) and (w <= z))) == 1:
#                     print(x, y, z, w, '1')
#Answer: xwzy
# 5
# https://dropmefiles.com/GrejH
# for n in range(10000):
#     r = bin(n)[2:]
#     r += str(r.count('1') % 2)
#     r += str(r.count('1') % 2)
#     if int(r, 2) > 55:
#         print(int(r, 2))
#         break
#Answer: 58
# 14
# https://dropmefiles.com/R36qC
# def calc(x, a, b):
#     s = ''
#     x = int(str(x), a)
#     while x > 0:
#         s += str(x // b)
#         x //= b
#     return s[::-1]
# chisl = (3*216**4) + (2*36**6) - 648
# d = calc(chisl, 10, 6)
#
# print(d.count('5'))
#Answer: 2
# 17
# В файле содержится последовательность из 10000 целых положительных чисел.
# Каждое число не превышает 10000.
# Определите и запишите в ответе сначала количество пар элементов последовательности,
# у которых сумма элементов кратна 10, затем максимальную из сумм элементов таких пар.
# В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.
# https://dropmefiles.com/Bg9w4
# arr = [int(x) for x in open('service_files/MODULETEST.txt')]
# count = 0
# maxx = float('-inf')
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         a = int(arr[i])
#         b = int(arr[j])
#         if (a + b) % 10 == 0:
#             count += 1
#             maxx = max(maxx, (a + b))
# print(count, maxx)
#Answer 4999742 19990