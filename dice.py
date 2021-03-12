import random

def roll_dice():
	a = random.randint(1 , 6)
	b = random.randint(1 , 6)
	return a + b

repeat = True
while repeat:
	input("Press ENTER To roll the dice")
	roll = roll_dice()
	if roll == 7 or roll == 11:
		print("You won")
	else:
		point = roll
		print("The point is now" , point , ".")
	print("Do you want to roll again? Type Y if you want to roll again or Type N if you want to exit from the program")
	repeat = "Y" in input()
