# not yet finished

import string
while True:
	try:
		s = input().split()
	except EOFError:
		break
	c = 0
	for word in s:
		word = ''.join(filter(lambda a: a not in string.punctuation, word))
		if word != '': c += 1
	print(c)