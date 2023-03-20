from collections import Counter

arr = []
file = open("9.csv")
for line in file:
	arr.append([int(x) for x in line.split(";")])

count = 0
for line in arr:
	info = Counter(line)
	if (list(info.values()).count(2) == 1 and list(info.values()).count(1) == 4) and (len(info.values()) == 5):
		k = list(info.keys())
		print(list(info.values()), k)
		if ((k[1] + k[2] + k[3] + k[4]) / 4) <= (k[0] * 2):
			count += 1
print(count)