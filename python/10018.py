for _ in range(int(input())):
	i = int(input())
	count = 0
	while str(i) != str(i)[::-1]:
		i = int(i + int(str(i)[::-1]))
		count += 1
	print(count, i)