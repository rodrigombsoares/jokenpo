def get_input():
	print('(R)ock, (P)aper, (S)cissors')
	return input('Choose your weapon: ')

def get_results(statement):
	results = statement.split("#")
	
	computer_hand = results[0]
	winner = results[1]
	return computer_hand, winner
		