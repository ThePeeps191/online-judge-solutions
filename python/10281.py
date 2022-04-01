# not yet finished

total = 0
speed = 0
time = 0

while True:
	try:
		l = input().split()
	except EOFError:
		break
	if len(l) == 2:
		_time = [int(a) for a in l[0].split(":")]
		time = _time[2] + 60 * _time[1] + 3600 * _time[0]
		speed = int(l[1])
	else:
		t = _time[2] + 60 * _time[1] + 3600 * _time[0]
		last_time = time
		time = t

		