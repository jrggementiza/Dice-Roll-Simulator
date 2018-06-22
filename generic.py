""" 
A Collection of Generic Code often encounterd in day to day use cases. 
"""

def run_again(run_again_prompt='Would you like to try again? [y / n]: ',
	end_message='Exiting Program. Good Bye.',
	error_prompt='[y / n] only please!: '
	):
	
	""" 
	Prompts user if they want to run the program again
	Returns True for 'y' (or 'yes') or False for 'n' (or 'no')
	"""

	while True:
		try:
			answer = input(run_again_prompt)
			answer = answer.lower()
			if answer == 'yes': answer = 'y'
			if answer == 'no': answer = 'n'

			assert answer == 'y' or answer =='n'

		except AssertionError:
			print(error_prompt)

		else:
			if answer == 'y':
				return True
			else:
				print(end_message)
				return False