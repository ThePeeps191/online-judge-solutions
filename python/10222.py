# bug, not yet finished

s = input().lower()
keyboard = [
	"`1234567890-=",
	"qwertyuiop[]\\",
	"asdfghjkl;'",
	"zxcvbnm,./"
]
o = ''
for k in keyboard:
	for char in s:
		if char != ' ':
			if char in k:
				i = k.index(char)
				o += k[i - 2]
		else:
			o += ' '
print(o)