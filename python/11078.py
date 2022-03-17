for _ in range(int(input())):
	s = int(input())
	scores = [int(input()) for _ in range(s)]
	max_diff = -999999999999999999999999
	cv = scores[0];
	for i in range(1, len(scores)):
		max_diff = max(max_diff, cv - scores[i])
		cv = max(cv, scores[i])
	print(max_diff)