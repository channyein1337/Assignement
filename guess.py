import random

def guess(low , high):
    print("Guess a number between {} and {}".format(low,high))
    num = random.randint(low,high)
    rounds = 10000
    for i in range(rounds):
        guess = input("Enter a number: ")
        try:
            integer = int(guess)
            if integer == num:
                print("Congrats You won!")
                print("You used {} rounds".format(i+1))
                print("Press Ctrl c if you want to exit from the program.")
            elif integer < num:
                print("Try Higher")
            elif integer > num:
                print("Try Lower")
        except ValueError:
            print("Please enter a valid integer")    
while True:
	guess(1,100)
	
	
	
