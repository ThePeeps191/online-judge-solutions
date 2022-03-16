# still in progress (wrong answer)

for _ in range(int(input())):
	case = input()
	last_number = 0
	count = 0
	for char in case:
		if char == 'X':
			last_number = 0
		else:
			last_number += 1
			count += last_number
	print(count)