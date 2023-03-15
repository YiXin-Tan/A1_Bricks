board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 2, 2, 2, 0, 0, 0]
]
zero_arr = []
one_arr = []
two_arr = []
three_arr = []
four_arr = []
five_arr = []
six_arr = []
seven_arr = []
index_vertical = 0
num = 0


while num < len(board):

    i = board[num]
    for index in i:
        index = 0
        index_in_i = 0

        # li = []
        while index < len(i):

            if i[index] == 1:
                # li.append(index)

                if i[index_in_i] == i[index_in_i+1] == i[index_in_i+2] == i[index_in_i+3]:
                    print(1)
                # li.clear()
            elif i[index] == 2:
                # li.append(index)
                if li[index_in_i] == li[index_in_i+1] == li[index_in_i+2] == li[index_in_i+3]:
                    print(2)
                # li.clear()

        index +=1


    if index == 0 and len(i)> index_vertical:
        zero_arr.append(i[index])








    # for index_vertical in board:
    #
    #     index_vertical = 0
    #     if index_vertical == 0:
    #         zero_arr.append(i[index_vertical])
    #
    #     elif index_vertical == 1:
    #         one_arr.append((i[index_vertical]))
    #
    #     elif index_vertical == 2:
    #         two_arr.append(i[index_vertical])

    num +=1



    # for one in board:
    #     one = 1
    #     one_arr.append((i[one]))
    #
    # for two in board:
