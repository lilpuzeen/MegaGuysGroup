# if (логическое выражение):
# 	...
# elif ():
#   ...
# elif (логическое выражение):
#   ...
# else:
# 	...

# Форматированные строки:

age = int(input())
name = input()

if age >= 18:
	print(f"Проходи {name}")  # f - formatted
elif age >= 16:
	print(f"На первый раз прощаю")
else:
	print(f"Пошел нахуй мелкий")
