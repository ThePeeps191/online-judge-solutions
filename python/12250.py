hello = {
	"HELLO" : "ENGLISH",
	"HOLA" : "SPANISH",
	"HALLO" : "GERMAN",
	"BONJOUR" : "FRENCH",
	"CIAO" : "ITALIAN",
	"ZDRAVSTVUJTE" : "RUSSIAN"
}
t = 1
while True:
	n = input()
	if n == "#": break
	print(f"Case {t}: {hello.get(n, 'UNKNOWN')}")
	t += 1