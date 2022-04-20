from random import choice

while True:
	choices = ['Rock','Paper','Scissors']
	print("What's Your Choice?\n0. Rock\n1. Paper\n2. Scissors")

	myChoice = choices[int(input())]
	opponentChoice = choice(choices)

	#print(myChoice, opponentChoice)

	if(myChoice == opponentChoice):
		print("Tie, so boring!")
	elif(myChoice == 'Scissors' and opponentChoice == 'Paper'):
		print("You Win!")
	elif(myChoice == 'Paper' and opponentChoice == 'Rock'):
		print("You Win!")
	elif(myChoice == 'Rock' and opponentChoice == 'Scissors'):
		print("You Win!")
	else:
		print("You Lose DumDum!")
		
	play_again = input("Play Again? (y/n): ")
	if play_again.lower() != "y":
		break
