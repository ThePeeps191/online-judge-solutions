keys = [
	"abc",
	"def",
	"ghi",
	"jkl",
	"mno",
	"pqrs",
	"tuv",
	"wxyz"
]

for i in range(int(input())):
	s = input()
	c = s.count(" ")
	s = s.replace(" ", "")
	for char in s:
		for k in keys:
			if char in k:
				c += k.index(char) + 1
	print(f"Case #{i + 1}: {c}")