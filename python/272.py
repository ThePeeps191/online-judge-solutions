# in progress

db_quotes = {
	True: "``",
	False: "''"
}
# s_quotes = {
# 	True: "`",
# 	False: "'"
# }

while True:
	try:
		t = input()
		last_left = False
		for char in t:
			if char == '"':
				last_left = not last_left
				print(db_quotes[last_left], end = '')
			else:
				print(char, end = '')
		print()
	except EOFError:
		break