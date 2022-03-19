def Prime(n):
	if n < 2:
		return False
	if n == 2:
		return True;	
	if n % 2 == 0:
		return False;
	sqrt = int(n ** 0.5)
	for i in range(3, sqrt, 2):#(int i = 3; i <= sqrt; i+=2)
		if n % i == 0:
			return False;
	return True

while True:
	n = int(input())
	if n == 0: break
	a, b = n, 0
	for i in range(n + 1):
		if Prime(i):
			a = i
			b = n - i
			if Prime(b) and i != 0 and i != n and a != b:
				# print(a, b)
				print(f"{n} = {a} + {b}")
				break
	else:
		print("Goldbach's conjecture is wrong.")