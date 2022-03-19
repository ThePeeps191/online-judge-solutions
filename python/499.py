from string import ascii_letters as l

while True:
	try:
		s = input()
	except EOFError:
		break
	occ = {a: s.count(a) for a in l}
	m = max(occ.values())
	chars = ['', '']
	for char in occ.keys():
		if occ[char] == m:
			if char.upper() == char:
				chars[0] += char
			else:
				chars[1] += char
	print(f"{''.join(chars)} {m}")