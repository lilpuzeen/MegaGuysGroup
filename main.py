# s = "Grisha Misha Ruslan"
# # slices => <str>[start:stop:step=1]
# print(s[0])  # -> G
# print(s[-1])  # -> n
# print(s[1:4])  # -> ris
# print(s[::2])  # only %2 elements
# print(s[::-1])  # <=> reverse
# print(s[:2])  # first two elements
# print(s[-2:])
# print(s[2::2])
# print(s[2:15:2])
#
# # arr = ["1", "2", "3", "4", "5"]
# # a = "".join(arr)
# # print(a)
#
# s = "arseniy"
# print(len(s))
# # len <=> length

# from math import sqrt
# # Генераторы списков
# arr1 = [i**2 for i in range(1, 11)]
# arr2 = [i**0.5 for i in range(1, 11)]
# arr3 = [i for i in range(1, 11) if i % 2 != 0]
arr4 = [(2*i - 1) for i in range(1, 11)]
s = "136548"
# arr5 = [int(i) for i in list(s)]
# заполнить arr квадратами чисел от 1 до 10 вкл.
# for i in range(1, 11):
# 	arr.append(i**2)

# print(help(list))
# print(dir(str))
