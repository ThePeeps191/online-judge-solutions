#in progress

for _ in range(int(input())):
	s = input()
	if s == '':
		print("Yes")
	else:
		left1, right1, left2, right2 = s.count("("), s.count(")"), s.count("["), s.count("]")
		if left1 == right1 and left2 == right2:
			print("Yes")
		else:
			print("No")