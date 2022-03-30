while True:
	try:
		s = input()
	except EOFError:
		break
	for char in s:
		print(chr(ord(char) - 7), end='')
	print()