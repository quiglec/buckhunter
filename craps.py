"""
Debugging program for buckhunter app. Run in terminal before running the real app so you can play some craps.
"""

import random
import math

random.seed()

def diceroll():
	input("Press Enter to roll dice")
	dice_1 = random.randint(1, 6)
	dice_2 = random.randint(1, 6)
	print('Dice roll is a ' + str(dice_1) + ' and a ' + str(dice_2) + '\n')
	return(dice_1, dice_2)

def dice_reader():
	x, y = diceroll()
	if x + y in [2, 3, 12]:
		return(0)
	elif x + y in [7, 11]:
		return(1)
	else:
		return(x + y)

def game_start():
	point = 0
	while point == 0:
		result = dice_reader()
		if result in [4, 5, 6, 8, 9, 10]:
			print('Point established as ' + str(result) + '\n')
			point = result
			break
		if result == 0:
			print('CRAPS!')
			break
		if result == 1:
			print('Pass Line Wins!')
			break
	
	if point != 0:
		while point != 0:
			x, y = diceroll()
			if x + y == 7:
				print('Pass Line Loses!')
				break
			if x + y == point:
				print('Pass Line Wins!')
				break	

game_start()