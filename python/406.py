def get_primes(n):
	sieve = [True] * (n // 2)
	for i in range(3, int(n ** 0.5) + 1, 2):
		if sieve[i // 2]:
			sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
	return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]

while True:
	try:
		N, C = [int(a) for a in input().split()]
	except EOFError:
		break
	l = get_primes(N)
	length = len(l)
	output = []
	if length % 2 == 0:
		pass
	else:
		middle = length // 2
		index = middle
		output.append(l[middle])
		
	print()
