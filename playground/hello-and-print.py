n = ["Deuce", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queue", "King"]
s = ["Spades", "Hearts", "Diamonds", "Clubs"]

for i, suit in enumerate(s):
	print('*'*80)
	print(f"Printing: {suit}")
	print('*'*80)
	for j, value in enumerate(n):
		print(f"{value} ({j+2}) of {suit}")