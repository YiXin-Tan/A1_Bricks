"""
FIT1045: Sem 1 2023 Assignment 1
"""
import random
import os

#hello
def clear_screen():
    """
    Clears the terminal for Windows and Linux/MacOS.

    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def print_rules():
    """
    Prints the rules of the game.

    :return: None
    """
    print("================= Rules =================")
    print("Connect 4 is a two-player game where the")
    print("objective is to get four of your pieces")
    print("in a row either horizontally, vertically")
    print("or diagonally. The game is played on a")
    print("6x7 grid. The first player to get four")
    print("pieces in a row wins the game. If the")
    print("grid is filled and no player has won,")
    print("the game is a draw.")
    print("=========================================")


def validate_input(prompt, valid_inputs):
    """
    Repeatedly ask user for input until they enter an input
    within a set valid of options.

    :param prompt: The prompt to display to the user, string.
    :param valid_inputs: The range of values to accept, list
    :return: The user's input, string.
    """
    valid_input = False
    while not valid_input:
        option = input(prompt)
        if option in valid_inputs:
            valid_input = True
            return option
        else:
            print('Invalid input, please try again.')


def create_board():
    """
    Returns a 2D list of 6 rows and 7 columns to represent
    the game board. Default cell value is 0.

    :return: A 2D list of 6x7 dimensions.
    """
    row_num = 6
    col_num = 7
    new_board = []

    for row_index in range(row_num):  # iterates for row_num (6) times to create row_num (6) rows
        row = [0] * col_num  # each row contains col_num (7) slots
        new_board.append(row)
    return new_board


def print_board(board):
    """
    Prints the game board to the console.

    :param board: The game board, 2D list of 6x7 dimensions.
    :return: None
    """
    board_str = ""  # initialize board (type str) to be returned
    header = "========== Connect4 ========="
    players = "Player 1: X       Player 2: O"
    margin = ""
    col_numbers = "  1   2   3   4   5   6   7"
    border_horizontal = " --- --- --- --- --- --- ---"
    board_str += "\n".join([header, players, margin, col_numbers, border_horizontal])  # each element will have it's own line

    for row in board:  # iterate through 6 rows in the board
        board_str += "\n|"
        for slot in row: # iterate through 7 slots in a row
            if slot == 0:  # checks if the slot is empty
                display_token = " "
            elif slot == 1:  # display "X" if player1's token exist in the slot
                display_token = "X"
            elif slot == 2:  # display "O" if player2's token exist in the slot
                display_token = "O"
            board_str += f" {display_token} |"
        board_str += ("\n" + border_horizontal)
    footer = "============================="
    board_str += ("\n" + footer)
    print(board_str)


def drop_piece(board, player, column):
    """
    Drops a piece into the game board in the given column.
    Please note that this function expects the column index
    to start at 1.

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player who is dropping the piece, int.
    :param column: The index of column to drop the piece into, int.
    :return: True if piece was successfully dropped, False if not.
    """
    row_index_to_check = 5  # start checking from bottom-most row, check bottom-up
    col_index_to_check = column - 1  # index of first column is 0, while player input is 1
    while row_index_to_check >= 0:
        slot_to_check = board[row_index_to_check][col_index_to_check]
        if slot_to_check == 0:
            board[row_index_to_check][col_index_to_check] = player
            return True
        row_index_to_check -= 1
    return False


def execute_player_turn(player, board):
    """
    Prompts user for a legal move given the current game board
    and executes the move.

    :return: Column that the piece was dropped into, int.
    """
    drop_successful = False

    while not drop_successful:
        validated_col_option = validate_input(
            f'Player {player}, please enter the column you would like to drop your piece into: ',
            ['1', '2', '3', '4', '5', '6', '7'])
        drop_successful = drop_piece(board, player, int(validated_col_option))
        if drop_successful:
            return validated_col_option
        print('That column is full, please try again.')


def end_of_game(board): # Task 6
	"""
	Checks if the game has ended with a winner
	or a draw.

	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
	"""

			
	# player has won
	player_has_won = get_winning_player(board) # this is either 0, 1 or 2
	if player_has_won != 0:
		return player_has_won
	
	# board is full
	if board_is_full(board):
		return 3

	# game is not over
	return 0


def board_is_full(board) -> bool:
	"""
	Checks if the board is full

	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: true if full else false
	"""
	
	"""
	check every number slot in board
	if any slot has a 0 then return false
	if no slot is 0 return True
	"""

	for row in board:
		for num in row:
			if num == 0:
				return False
	return True
		

def get_winning_player(board) -> int:
	"""
	Checks if there is a winning player

	:param board: The game board, 2D list of 6 rows x 7 columns.
	:return: 0 if no winner, 1 if player 1 wins, 2 if player 2 wins
	"""
	# i = 0 
	# j = 0
	# element = board[i][j]

	"""
	check horizontal:
	1. Go through each row in board
	2. For each row:
		a) check if any 4 adjacent slots are equal to each other 
			i) if they are equal: 
				return 1 if slots have 1s in them
				return 2 if slots have 2s in them

	"""

	# Checks if numbers in each row are not 1 or 2 (i.e no winners)
	# for row in board:
	# 	for i in range(len(row)-3):
	# 		if row[i] != 1 or row[i] != 2:
	# 			return 0

	
	# Checking for horizontal win
	for row in board:
		# we subtract 3 from the length of the row as we only need to check 4 adjacent slots
		# looking at a row [0, 0, 0, 0, 0, 0, 0]
			# if we start at i=0, the first 4 slots will be checked (0,1,2,3)
			# if we then go to i=1, indexes 1,2,3,4 will be checked
				# continuing this cycle we want to stop when we cant check 4 slots, (i.e when i= 4, 5, 6) otherwise out of range error will occur
		for i in range(len(row)-3):
			if row[i] == row[i+1] == row[i+2] == row[i+3] == 1:
				return 1
			elif row[i] == row[i+1] == row[i+2] == row[i+3] == 2:
				return 2
	
	
	

	# Checking for vertical win 
	# this will be the range of the first row, as board[0] is row 1
	# so we are iterating through the range of 7 (0 to 6)
	for i in range(len(board[0])):

		# Remember that length of board is the number of rows in the board. (board is a list of lists)
		# subtract 3 is same reason for testing horizontally 
		for j in range(len(board)-3):
			# print(len(board)): will output 6 for 6 rows

			# index 'j' increments for each test as we are moving down 1 row for every j+1 (testing vertically)
			if board[j][i] == board[j+1][i] == board[j+2][i] == board[j+3][i] == 1:
				return 1
			elif board[j][i] == board[j+1][i] == board[j+2][i] == board[j+3][i] == 2:
				return 2

	

	# Checking diagonal wins
	# subtract 3 from length of board as only need to iterate to 3rd row
		# at rows 4-6, and go diagonally down to the right there are only 3, 2, and 1 blocks adjacent (so cannot be any wins here)
	for i in range(len(board)-3):
		
		# 7 elements in each row. last element where there can be a win diagonally to the right is at board[0][3], i.e element 4
			# from elements 5-7, check diagonally down to the right, there are only 3, 2 and 1 blocks respectively adjacent
		for j in range(len(board[0])-3):

			"""
			these 'for loops' have created a rectangle: 4 to the right and 3 down in the board starting at [0][0] (as a range for where diagonals can be checked from)
			- the same will be done for checking diagonals right to left
			"""
			

			# right to left diagonal win

			if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == 1:
				return 1
			elif board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == 2:
				return 2

			
			# left to right diagonal win
			# -j as we want to start from right side (i.e board[0][6])
				# if j = 0, then -j = -0
				# if j = 1, then -j = -1
				# so on
			# i remains the same as adding 1 to the index will still go down a row
			
			if board[i][-j-1] == board[i+1][-j-2] == board[i+2][-j-3] == board[i+3][-j-4] == 1:
				return 1
			elif board[i][-j-1] == board[i+1][-j-2] == board[i+2][-j-3] == board[i+3][-j-4] == 2:
				return 2
				
		# Return 0 (no winner yet): this is outside each 'for loop' (let loops iterate first, if no winner found then only return 0)
	return 0

def local_2_player_game():
	"""
	Runs a local 2 player game of Connect 4.

	:return: None
	"""
	# Implement your solution below
	board = create_board()
	
    # initial player is assigned 1
	current_player = 1 
	# There is no previous column choice to tell players
	prev_col_choice = None

	while True:
		clear_screen()
		# execute the turn
		print_board(board)

		# if there was a previous move (turn 1 has no previous move), then print that out
		if prev_col_choice:
			# '2 if current_player==1 else 1' only switches player inside print function
			print(f'Player {2 if current_player==1 else 1} has dropped in {prev_col_choice}')

		prev_col_choice = execute_player_turn(current_player, board)
		
		check_winner = end_of_game(board)
		if check_winner == 1:
			clear_screen()
			print_board(board)
			print("Player 1 wins")
			break
		elif check_winner == 2:
			clear_screen()
			print_board(board)
			print("Player 2 wins")
			break
		elif check_winner == 3:
			clear_screen()
			print_board(board)
			print("Draw")
			break

		# change the Player
		current_player = 2 if current_player == 1 else 1


def main():
	"""
	Defines the main application loop.
    User chooses a type of game to play or to exit.

	:return: None
	"""
	menu_string = """=============== Main Menu ===============
Welcome to Connect 4!
1. View Rules
2. Play a local 2 player game
3. Play a game against the computer
4. Exit
=========================================
Enter a number: """
	clear_screen()
	while True:
		user_input = validate_input(
			prompt=menu_string,
			valid_inputs=["1", "2", "3", "4"]
		)
		if user_input == "1":
			clear_screen()
			print_rules()
		if user_input == "2":
			return local_2_player_game()
		if user_input == "3":
			return game_against_cpu()
		if user_input == "4":
			print("You have exited the game")
			return


def cpu_player_easy(board, player):
	"""
	Executes a move for the CPU on easy difficulty. This function 
	plays a randomly selected column.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	cpu_has_dropped = False
	while not cpu_has_dropped:
		ran_int = random.randint(1, 7)
		cpu_has_dropped = drop_piece(board, player, ran_int)	
		if cpu_has_dropped:
			return ran_int

def clone_board(board):
	"""
	Creates a deep clone of the param board

	:param board: the board
	:return: cloned board
	"""
	# create board of same number of rows and height
	cloned_board = create_board()
	# for each item in the param board, copy over to cloned board

	for i in range(len(board)):
	# for each value in each row
		for j in range(len(board[0])):
			cloned_board[i][j] = board[i][j]
	return cloned_board


	# return the cloned board 
	
def cpu_player_medium(board, player):
	"""
	Executes a move for the CPU on medium difficulty.
	It first checks for an immediate win and plays that move if possible. 
	If no immediate win is possible, it checks for an immediate win 
	for the opponent and blocks that move. If neither of these are 
	possible, it plays a random move.

	:param board: The game board, 2D list of 6x7 dimensions.
	:param player: The player whose turn it is, integer value of 1 or 2.
	:return: Column that the piece was dropped into, int.
	"""
	
	"""
	1. Play a move that results in immediate win
	2. Check if oppenent can score immediate win
		block this 
	3. if none then play random drop
	"""
	
	# for each col
	# clone the board
	# drop the piece into the cloned board
	# if this wins the game, drop the piece into the real board and return the column

	for j in range(len(board[0])):
		# print(j)
		cloned_board = clone_board(board)
		cpu_drop = drop_piece(cloned_board, player, j)
		if cpu_drop:
			if get_winning_player(cloned_board) == player:
				drop_piece(board, player, j)
				return j

	# check opponent block
	for j in range(len(board[0])):
		cloned_board = clone_board(board)
		opponent = 2 if player == 1 else 1
		player_win = drop_piece(cloned_board, opponent, j)
		if player_win:
			if get_winning_player(cloned_board) == opponent:
				drop_piece(board, player, j)
				return j

	# for i in range(len(board)):
	# 	for j in range(len(board[0])):
	# 		if board[i][j] == 0:
	# 			board[i][j] = player_piece
	# 			if get_winning_player == player_piece:
	# 				board[i][j] = cpu_piece
	# 				return cpu_piece
	
	return cpu_player_easy(board, player)




def cpu_player_hard(board, player):
    """
    Executes a move for the CPU on hard difficulty.
    This function creates a copy of the board to simulate moves.
    <Insert player strategy here>

    :param board: The game board, 2D list of 6x7 dimensions.
    :param player: The player whose turn it is, integer value of 1 or 2.
    :return: Column that the piece was dropped into, int.
    """
    # Implement your solution below
    raise NotImplementedError


def get_cpu_difficulty() -> int:
	"""
	Gets the difficulty of the CPU
	Asks the user what difficulty they would like to play against

	:return int: 1 = easy, 2 = medium, 3 = hard
	use validate_input
	"""
	
	user_input = int(validate_input(prompt = "Please select a difficulty (1: Easy, 2: Medium, 3; Hard): ", valid_inputs = ["1", "2", "3"]))
	return user_input

def game_against_cpu():
	"""
	Runs a game of Connect 4 against the computer.

	:return: None
	"""
	board = create_board()
	
    # initial player is assigned 1
	current_player = 1 
	# There is no previous column choice to tell players
	prev_col_choice = None

	# get cpu difficulty (1 = easy, 2 = med, 3 = hard)
	cpu_difficulty: int = get_cpu_difficulty()

	while True:
		clear_screen()
		# execute the turn
		print_board(board)

		# if there was a previous move (turn 1 has no previous move), then print that out
		if prev_col_choice:
			# '2 if current_player==1 else 1' will only switch player inside print function as current_player switched at bottom of function
			print(f'Player {2 if current_player== 1 else 1} has dropped in {prev_col_choice}')

		if current_player == 1:
			prev_col_choice = execute_player_turn(current_player, board)
		elif current_player == 2:
			# this is the cpu turn

			# Easy difficulty
			if cpu_difficulty == 1:
				prev_col_choice = cpu_player_easy(board, current_player)

			if cpu_difficulty == 2:
				prev_col_choice = cpu_player_medium(board, current_player)

			if cpu_difficulty == 3:
				print("Not implemented yet")
				return
		
		check_winner = end_of_game(board)
		if check_winner == 1:
			clear_screen()
			print_board(board)
			print("Player 1 wins")
			break
		elif check_winner == 2:
			clear_screen()
			print_board(board)
			print("Player 2 wins")
			break
		elif check_winner == 3:
			clear_screen()
			print_board(board)
			print("Draw")
			break

		# change the Player
		current_player = 2 if current_player == 1 else 1


if __name__ == "__main__":
    main()
