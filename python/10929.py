while True:
	i = int(input())
	if i == 0:
		break
	if i % 11 == 0:
		print(f"{i} is a multiple of 11.")
	else:
		print(f"{i} is not a multiple of 11.")