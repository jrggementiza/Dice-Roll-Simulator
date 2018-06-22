""" Generic Dice Rolling Simulator """

import random, time, generic


def roll_results(dice_collection):
	print('ROLLING DICE... ')
	time.sleep(1)
	for dice_number, dice_value in enumerate(dice_collection):
		print(f'Dice {dice_number + 1} rolled {dice_value}')

def play(number_of_dice=2, number_of_sides=6):
	dice_collection = [random.randrange(1, number_of_sides) for i in range(0, number_of_dice)]
	roll_results(dice_collection)

def main():
	run_game = True
	while run_game == True:
		play()
		run_game = generic.run_again('Would you like to roll again? ', 'Exiting program. Good Bye.')

if __name__ == '__main__':
	main()

