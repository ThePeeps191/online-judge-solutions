keys = {
	"ABC" : 2,
	"DEF" : 3,
	"GHI" : 4,
	"JKL" : 5,
	"MNO" : 6,
	"PQRS" : 7,
	"TUV" : 8,
	"WXYZ" : 9
}

while True:
	try:
		s = input()
	except EOFError:
		break
	for char in s:
		for k in keys:
			if char in k:
				print(keys[k], end='')
				break
		else:
			print(char, end='')
	print()