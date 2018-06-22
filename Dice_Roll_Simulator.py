""" Generic Dice Rolling Simulator 

To Add:
Set number of dice and sides per dice
"""

import random, time, generic


def rollDice():
	print('ROLLING THE DICE NOW....')
	time.sleep(2)
	diceResults = [random.randrange(1,6) for i in range(0,2)]
	print('YOU ROLLED : {0} {1}'.format(diceResults[0], diceResults[1]))

def play():
	runGame = True
	while runGame == True:
		rollDice()
		runGame = generic.run_again()

def main():
	play()

if __name__ == '__main__':
	main()