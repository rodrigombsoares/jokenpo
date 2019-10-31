from random import randint

hands = ['rock', 'paper', 'scissors']
hands_map = {'r' : 'rock', 'p': 'paper','s':'scissors'}

def rand_hand():
	return hands[randint(0,2)]

def handle_hand(player_hand):
	player_hand.lower()
	if(player_hand not in hands):
		return hands_map[player_hand]
	return player_hand



def get_winner(p_hand, pc_hand):
	"""
	Generates a tuple with player hand and pc hand
	
	Get hands index and check the the delta:
		when result is negative, the winner hands 
		is in the exact tuple position as delta index
		(r,p) = 0,1 = (-1) -> p = 1 or -1
		(r,s) = 0,2 = (-2) -> r = 0 or -2
		(p,s) = 1,2 = (-1) -> s = 2 or -1
		
		when delta is positive, we subtract 3 and
		get the winner hand in the exact tuple position
		(p,r) = 1,0 = (1)-3 = -1 -> p = 1 or -1
		(s,r) = 2,0 = (2)-3 = -2 -> r = 0 or -2
		(s,p) = 2,1 = (1)-3 = -1 -> s = 2 or -1
	"""
	table = (p_hand, pc_hand)
	delta = hands.index(p_hand) - hands.index(pc_hand)
	
	if delta == 0:
		return 'tie'
	elif delta < 0:
		winner = table[delta]
		return winner + ' wins'
	elif delta > 0:
		winner = table[delta-3]
		return winner + ' wins'

