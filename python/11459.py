from itertools import cycle

for _ in range(int(input())):
	a, b, c = [int(i) for i in input().split()]

	# Snakes and Ladder game
	snaks_lads = [[int(i) for i in input().split()] for _ in range(b)]
	dice_rolls = [int(input()) for _ in range(c)]

	players = [1 for _ in range(a)]
	player_c = cycle([i for i in range(a)])
	for index in range(c):
		roll = dice_rolls[index]
		player = next(player_c)
		# print(player)
		players[player] += roll
		for snak_lad in snaks_lads:
			# print(snak_lad)
			if snak_lad[0] == players[player]:
				players[player] = snak_lad[1]
				break
	for x in range(1, a + 1):
		print(f"Position of player {x} is {players[x - 1]}.")