board = [
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [1, 2, 2, 2, 0, 0, 0]
]

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0



for i, num in board:
    i = board[num]
    for e in i:
        a = 0

        li = []
        if i[e] == 1:
            li.append(e)

            if li[a] == li[a+1] == li[a+2] == li[a+3]:
                print(1)
            li.clear()
        elif i[e] == 2:
            li.append(e)
            if li[a] == li[a+1] == li[a+2] == li[a+3]:
                print(2)
            li.clear()