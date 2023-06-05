from itertools import product, permutations

# 7667
# count = 0
#
# for string in product("ЕГЭ", repeat=5):
# 	if string[0] in ["Е", "Э"]:
# 		count += 1
# print(count)

# 7921
# count = 0
# for string in product("ГОД", repeat=6):
# 	if string[0] in ["Г", "Д"]:
# 		count += 1
# print(count)


# 47212
# count = 0
# # bin -> 2CC
# # oct -> 8CC
# # hex -> 16CC
# # 1 3 5 7
# for i in range(8**4, 8**5):
# 	m = oct(i)[2:].replace("3", "1").replace("5", "1").replace("7", "1")
# 	if (m.count("6") == 1) and ("16" not in m) and ("61" not in m):
# 		count += 1
# print(count)

# 27539
# count = 0
# for string in product("БОРИС", repeat=6):
# 	if (string.count("Б")== 1) and (string.count("Р") == 1) and (string.count("С") <= 1):
# 		count += 1
# print(count)

# 3205
# for index, string in enumerate(product("АОУ", repeat=5)):
# 	if string[0] == "О":
# 		print(index + 1)
# 		break

# 13594
# count = 0
# for string in product("АВСХ", repeat=5):
# 	if (string[-1] == 'Х' and string.count('Х') == 1) or ('Х' not in string):
# 		count += 1
# print(count)

# 3518
# print(list(product("АМРТ", repeat=4))[249])

# 47005
# restricted = set()
# for soglas in product("ПРБЛ", repeat=2):
# 	for glas in product("ОА", repeat=2):
# 		restricted.add("".join(soglas))
# 		restricted.add("".join(glas))
#
# words = set()
# for string in permutations("ПАРАБОЛА", r=8):
# 	word = "".join(string)
# 	if all(x not in word for x in restricted):
# 		words.add(word)
#
# print(len(words))

# 48456
# def calc(x, a, b):
# 	s = ""
# 	x = int(str(x), a)
# 	while x > 0:
# 		s += str(x % b)
# 		x //= b
# 	return s[::-1]
#
#
# count = 0
# for i in range(9**5, 9**6):
# 	m = calc(i, 10, 9).replace("3", "1").replace("5", "1").replace("7", "1")
# 	if m.count("4") == 1 and m.count("1") == 2:
# 		count += 1
# print(count)
