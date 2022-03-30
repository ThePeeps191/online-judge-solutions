while True:
	try:
		s = input()
	except EOFError:
		break
	o = ['']
	index = 0
	for char in s:
		if char not in '[]':
			o.insert(index, char)
			index += 1
		else:
			if char == '[':
				index = 0
			else:
				index = len(o) - 1
	print(*o, sep='')