# not yet finished

while True:
	try:
		nums = [int(a) for a in input().split()]
	except EOFError:
		break
	diffs = []
	for i in range(len(nums) - 1):
		diffs.append(abs(nums[i] - nums[i + 1]))
		#print(diffs, list(range(1, len(nums) - 1)))
	print('Jolly' if sorted(set(diffs)) == list(range(1, len(nums) - 1)) else 'Not jolly')