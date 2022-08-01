from collections import Counter
l = []
while True:
	try:
		l += [int(a) for a in input().split()]
	except EOFError:
		break
nums = Counter(l)
for x in list(nums):
	print(x, nums[x])