def tr(start, stop):
	if start > stop:
		return 0
	if start == stop:
		return 1
	if start == 17:
		return 0
	return tr(start + 1, stop) + tr(start * 2, stop)


print(tr(1, 10) * tr(10, 35))
