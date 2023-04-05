valid_rows = []
valid_columns = []
valid_players = []
valid_token_wins = []
valid_cpu_num = []
column_choices= []
for i in range(4, 51):
    valid_rows.append(str(i))
    valid_columns.append(str(i))
for i in range(2, 11):
    valid_players.append(str(i))
    valid_cpu_num.append(str(i))
for i in range(4, 11):
    valid_token_wins.append(str(i))


def get_user_inputs(prompt, valid_inputs):
    #user_input is assigned to an input with the prompt string inside it
    user_input = input(prompt) 
    #while whatever the user inputs is not in the list do the following
    while user_input not in valid_inputs:
        #print this string
        print("Invalid input, please try again.")
        #re ask for input from the user
        user_input = input(prompt)
        #return the user_input
    return user_input

column_num = get_user_inputs(prompt="Enter a number of columns for the gameboard (4-50): ", valid_inputs = valid_rows)
row_num = get_user_inputs(prompt= "Enter a number of rows for the gameboard (4-50):  ", valid_inputs = valid_columns)
num_players = get_user_inputs(prompt="Enter a number of local players (2-10): ", valid_inputs = valid_players)
token_win = get_user_inputs(prompt="Enter the number of tokens adjacent for a player to win (4-10): ", valid_inputs = valid_token_wins)

for i in range(int(column_num)+1):
    column_choices.append(str(i))

def create_board():

    #list for columns with length of 7
    num_of_columns = column_num
    #list for rows
    num_of_rows = row_num

    game_board = []

    for i in range(int(row_num)):
        row = [0] * int(column_num)
        game_board.append(row)
    return game_board


def print_board(board):
    # Assigning variables
    board_string = ""
    header = ("===" * (int(row_num)//int(2)) + " Connect4 " + "===" * (int(row_num)//int(2))) + "=="
    players = "Player 1: X       Player 2: O"
    line_break = ""
    column_nums = ("  "+"   ".join([str(i+1) for i in range(len(board[0:]))]))
    horizontal_line = " ---" * int(row_num)
    footer = "====" * int(row_num) + "="
    # .join can only work on multiple variables if they are in a list
    # \n = newline
    board_string = "\n".join([header, players, line_break, column_nums, horizontal_line]) 


    # iterate through rows in the 2D array
    for row in board:
        
        # adds a | for every row (left most box only)
        board_string += "\n|"

        for num in row:
            display_char = get_display_char(num)
            board_string += f" {display_char} |"

        # Add horizontal line for each row
        board_string += ("\n" + horizontal_line)
    board_string += ("\n" + footer)
    print(board_string)


def get_display_char(num):
    """
    Gets display character for a number on the board
    """
    char_list = [' ', 'X', 'O', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    return char_list[num]

def drop_piece(board, player, column: int):
    
    check_column = column - 1
    check_row = int(row_num) - 1


    while check_row >= 0:
        check_slot = board[check_row][check_column]
        if check_slot == 0:
            board[check_row][check_column] = player
            return True
        #decrement check_row
        check_row -= 1
    return False

def execute_player_turn(player, board): # Task 5

    # initial value of successful_drop
    successful_drop = False
    
    while successful_drop == False:

        # Column choice is assigned function validate input, prompting the specific player
        column_choice = get_user_inputs(f'Player {player}, please enter the column you would like to drop your piece into: ', valid_inputs = column_choices )
        
        # Reassign successful_drop to drop_piece
        successful_drop = drop_piece(board, player, int(column_choice))
        # print(successful_drop)
        
        if successful_drop == True:

            #use int() as column_choice choice has class string 
            return int(column_choice)
        print("That column is full, please try again.")

def end_of_game(board): # Task 6
    """
    Checks if the game has ended with a winner
    or a draw.

    :param board: The game board, 2D list of 6 rows x 7 columns.
    :return: 0 if game is not over, 1 if player 1 wins, 2 if player 2 wins, 3 if draw.
    """

            
    # player has won
    player_has_won = get_winning_player(board) 
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

    :param board: The game board, 2D list of x rows * y columns.
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
    winning_length = int(token_win)

    # check horizontal
    # Iterate through each row in the board
    for row in board:
        # Iterate through range of whatever the row is (gotten by user) - winning length (token_win: user input)
        for i in range(len(row)-winning_length):

            # store the number we are looking at here and initialise it with nothing stored 
            stored_num = None 

            # Iterate through range(starting index of row, starting index + winning length)
                # We do this as we dont know how many indexes in the row we have to check. If we did we could hard code it like we did in task 6 for checking horizontal wins
                # So in this case we loop it 
            for j in range(i, i+winning_length):
                # start at the first index in the row 
                current_num = row[j]

                # check if we have started storing
                # If there is no number stored in stored_num then store current_num
                if stored_num is None:
                    stored_num = current_num
                
                # If numbered stored is the same as the next number after it then continue checking
                elif stored_num == current_num and current_num !=0:
                    continue
                # if it is not a equal string of numbers or we find a zero, there is no winner here
                elif current_num != stored_num or current_num == 0:
                    stored_num = None
                    break
            # check if we have a winner (the whole row was the same when checking)
            if stored_num is not None:
                return stored_num

    # Checking vertical win
    for i in range(len(board[0])):
        for j in range(len(board)-winning_length):
            stored_num = None
            for k in range(j, j+winning_length):

                current_num = board[k][i]

                # check if we have started storing
                # If there is no number stored in stored_num then store current_num
                if stored_num is None:
                    stored_num = current_num
                
                # If numbered stored is the same as the next number after it then continue checking
                elif stored_num == current_num and current_num !=0:
                    continue
                # if it is not a equal string of numbers or we find a zero, there is no winner here
                elif current_num != stored_num or current_num == 0:
                    stored_num = None
                    break
            # check if we have a winner (the whole row was the same when checking)
            if stored_num is not None:
                return stored_num
    

   # Check diagonal left to right
    for i in range(len(board) - winning_length + 1):
        for j in range(len(board[0]) - winning_length + 1):
            stored_num = None
            for k in range(winning_length):
                current_num = board[i+k][j+k]

                # check if we have started storing
                # If there is no number stored in stored_num then store current_num
                if stored_num is None:
                    stored_num = current_num
                
                # If numbered stored is the same as the next number after it then continue checking
                elif stored_num == current_num and current_num !=0:
                    continue
                # if it is not a equal string of numbers or we find a zero, there is no winner here
                elif current_num != stored_num or current_num == 0:
                    stored_num = None
                    break
            # check if we have a winner (the whole row was the same when checking)
            if stored_num is not None:
                return stored_num

    # Check diagonal right to left
    for i in range(len(board) - winning_length + 1):
        for j in range(len(board[0]) - winning_length + 1):
            stored_num = None
            for k in range(winning_length):
                    current_num = board[i+k][-j-winning_length]

                    # check if we have started storing
                    # If there is no number stored in stored_num then store current_num
                    if stored_num is None:
                        stored_num = current_num
                
                    # If numbered stored is the same as the next number after it then continue checking
                    elif stored_num == current_num and current_num !=0:
                        continue
                    # if it is not a equal string of numbers or we find a zero, there is no winner here
                    elif current_num != stored_num or current_num == 0:
                        stored_num = None
                        break
                # check if we have a winner (the whole row was the same when checking)
            if stored_num is not None:
                return stored_num


    

   
            

    
    





if __name__ == "__main__":
    # Enter test code below
    board = create_board()
    move = execute_player_turn(1, board)
    print_board(board)
    print(move)






