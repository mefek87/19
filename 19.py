#minesweeper
import random
print("Welcome to minesweeper")
print("Please choose the board dimensions and the difficulty level:")
#choose_size
width = int(input("Declare width of the board:"))
height = int(input("Declare height of the board:"))
#choose_difficulty
difficulty_status=False
while  difficulty_status==False:
	print("Please type in the difficulty level (easy, medium or hard):")
	difficulty = str(input("Chosen difficulty:"))
	if difficulty == "easy":
		difficulty_status = True
	elif difficulty == "medium":
		difficulty_status = True
	elif difficulty =="hard":
		difficulty_status = True
	else:
		difficulty_status = False
print("Let's begin!")
#game_setup
if difficulty == "easy" :
	mines_qt = 0.1
elif difficulty == "medium" :
	mines_qt = 0.2
elif difficulty == "hard" : 
	mines_qt = 0.4
mines_number = int(int(width)*int(height)*mines_qt)
	#print(difficulty)
	#print(mines_qt)
	#print(mines_number)
#board_initial_setup
board = []
row = int(width)
col = int(height)
for x in range (0, row): 
  board.append([])
  for y in range(0, col):
    board[x].append(str(x) + str(y))
print(*board, sep="\n")
#mine_generator
mines_list = ["mine","mine"]
while len(mines_list)!=len(set(mines_list)):
	mines_list = []
	for i in range(mines_number):
		mines_list.append(str(random.randint(0,int(width)-1)) + str(random.randint(0,int(height)-1)))
#print(mines_list)
mines_left = len(mines_list)
#main_game
game_state = 1
bets=[]
while game_state == 1:
	print("Mines left: ",mines_left)
	print("Type in your bet as xy coordinates. For mine selection, type 'xy_mine'.")
	bet = str(input("Your bet: "))
#death condition	
	if str(bet) in mines_list:
		game_state = 0
		print("BOOM! YOU'RE DEAD!")
		print("Try again some other time!")
#game loop condition
	else:
		game_state = 1
		row=bet[0]
		col=bet[1]
#for mine selection
		if len(bet) > 2:
			mines_left -=1
			board[int(row)][int(col)] = "|>"
#for normal bet		
		else:
			adjacent_x = []
			adjacent_y = []
			adjacent_list=[]
			for x in range (-1,2):
				adjacent_x.append(int(row) + int(x))
			for y in range (-1,2):
				adjacent_y.append(int(col) + int(y))
			for x in adjacent_x:
				for y in adjacent_y:
					adjacent_list.append(str(x) + str(y))
			for element in mines_list:
				if element in adjacent_list:
					adjacent_list.remove(element)
			#print(adjacent_list)
			adjacent_sum= 9 - int(len(adjacent_list))
			board[int(row)][int(col)] = "#" + str(adjacent_sum)
		#game_state = 0
		#print("You found all the bombs! Bravo!")
		print("Good work, try again.")
		print(*board, sep="\n")