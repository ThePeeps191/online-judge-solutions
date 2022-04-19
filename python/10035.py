while True:
	a, b = [int(i) for i in input().split()]
	if [a, b] == [0, 0]:
		break
	length = min(len(str(a)), len(str(b)))
	if len(str(a)) != length:
		a = int(str(a)[len(str(a))-3:])
	if len(str(b)) != length:
		b = int(str(b)[len(str(b))-3:])
	count = 0
	last_carry = 0
	for i, j in zip(str(a)[::-1], str(b)[::-1]):
		i, j = int(i), int(j)
		if i + j + last_carry >= 10:
			count += 1
		last_carry = 1 if (i + j >= 10) else 0
	if count == 0:
		print("No carry operation.")
	elif count == 1:
		print("1 carry operation.")
	else:
		print(count, "carry operations.")