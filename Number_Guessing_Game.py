import random

def GenerateNumber(start=0, stop=20, step=1):
	return random.randrange(start,stop,step)

def GreetMessage():
	print("Welcome to the Number Guessing Game. \n\n")
	print("Description:\n")
	print("You have to guess a number from a given range. If it matches with the computer generated number then, You Win !\n")
	print("\tTo exit type(e|E).")

def gamePlay():
	GreetMessage()
	name = input("Enter your name:\t")
	rand_number = GenerateNumber(random.randint(1,9), random.randint(63,80), random.randint(3,8)) # using random numbers to generate a challenging number
	print("The Computer has generated a number. ");print(rand_number)
	user_choice = input("Enter your choice between (0|100):\t")
	# loop to match and take choices from user
	while user_choice != ("e" or "E"):
		user_choice = int(user_choice)
		if user_choice == rand_number:
			print(f"Congratulations ! {name}. You have WON !\t")
			break
		elif (user_choice <= rand_number + 5) and (user_choice >= rand_number - 5):
			if user_choice < rand_number:
				print(f"OOPS ! You have guessed wrong but you are near. Try thinking a bit greater than {user_choice}.")
			elif user_choice > rand_number:
				print(f"OOPS ! You have guessed wrong but you are near. Try thinking a bit a smaller than {user_choice}.")
		else:
			print("OOPS ! You have guessed wrong.\t")
		user_choice = input("Enter your choice:\t")



gamePlay()

# This Project is fully made. Please upload this project on github as a beginner level project.

# Version 2 of this project will be with colors and GUI.


