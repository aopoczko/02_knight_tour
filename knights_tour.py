
def draw_board(): #draw actual board state with formatting - not used in later stages

    dash_bar()

    for i in range(b):
        #print("".join([str(b - i).rjust(cell - 1), "|"]))
        print("".join([str(b - i).rjust(cell - 1), "|"]), " ".join([board[i][j].rjust(len(str(a * b)), "_") if board[i][j] != "X" else board[i][j].rjust(len(str(a * b)))  for j in range(a)]), "|")
        #print(" ".join(board[i]).rjust(cell, "_"))
        #print(i)
        #print("".join([str(b - i).rjust(cell - 1), "|"]), " ".join([(board[i][j].rjust(cell, "_")) for j in range(a)]), "|")
    dash_bar()
    #print(" " * (cell - 1), "-" * ((len(str(a * b)) + 1) * a), "---", sep = "")
    print(" " * (len(str(a)) +1), " ".join([(str(r+1).rjust(len(str(a * b)))) for r in range(a)]))
    #print(" ".join(["_" * len(str(a*b)) for _ in range(b)]))

def check_moves(): #marks available moves on the board

    count = 0
    moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]] #movement vectors from current position [x, y]
    for i in range(8):
        #for j in range(2):
        if y + moves[i][0] > b or y + moves[i][0] < 0 or x + moves[i][1] > a or x + moves[i][1] < 0:
            continue
        else:
            try:
                if board[y + moves[i][0]][x + moves[i][1]] == "_":
                    board[y + moves[i][0]][x + moves[i][1]] = str(count_moves(y + moves[i][0], x + moves[i][1]))
                    count += 1
                    print(f"ok  {moves[i]}")

            except:
                continue

    #print()
    #print(" " * (cell - 1), "-" * ((cell + 1) * a), "---", sep = "")

    dash_bar()
    for i in range(b):
        print("".join([str(b - i).rjust(cell - 1), "|"]), " ".join([board[i][j].rjust(len(str(a * b)), "_") if board[i][j] == "_" else board[i][j].rjust(len(str(a * b)), " ")  for j in range(a)]), "|")
    dash_bar()
    print(" " * (len(str(a)) + 1), " ".join([(str(r + 1).rjust(cell)) for r in range(a)]))
    #print(" ".join(["_" * len(str(a*b)) for _ in range(b)]))

    #print(x, y)
    return count

def count_moves(y, x): #subfunciton for check_moves(), counts available moves from tiles determined in master function
    moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
    count = 0
    #print("x:",x , "y:", y)
    for i in range(8):
        #for j in range(2):
        if y + moves[i][0] > b or y + moves[i][0] < 0 or x + moves[i][1] > a or x + moves[i][1] < 0:
            continue
        else:
            try:
                if board[y + moves[i][0]][x + moves[i][1]] == "_":
                    #print(x + moves[i][1], y + moves[i][0])
                    count += 1
                    #print(f"ok  {moves[i]}")
                    #print(f"ok {moves[i][0]}, {knight_x + moves[i][1]}")
            except:
                continue
    return count

def dash_bar(): #draw top and bottom --- line
    print(" " * (cell - 1), "-" * ((len(str(a * b)) + 1) * a), "---", sep="")

def ask_board(): #ask user for board dimensions
    while True:
        dim = input("Enter your board dimensions: ")
        try:
            a, b = dim.split(" ", 1)
        except ValueError:
            print(invalid_dim)
            continue

        if a.isnumeric() == False or b.isnumeric() == False:
            print(invalid_dim)
            continue
        elif len(dim.split(" ")) != 2:
            print(invalid_dim)
            continue
        elif int(a) < 1 or int(b) < 1:
            print(invalid_dim)
            continue
        else:
            return int(a), int(b)

def ask_pos(): #ask user about knight's starting position

    while True:
        pos = input("Enter the knight's starting position: ")
        try:
            x, y = pos.split(" ", 1)
        except ValueError:
            print(invalid_pos)
            continue

        if x.isnumeric() == False or y.isnumeric() == False:
            print(invalid_pos, "num")
            continue
        elif len(pos.split(" ")) != 2:
            print(invalid_pos, "split err")
            continue
        elif int(x) not in range(1, a + 1) or int(y) not in range(1, b + 1):
            print(invalid_pos, "range 1 - b")
            continue
        else:
            return int(x) - 1, b - int(y)

def ask_move(): #ask user about knight's next move

    moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
    pos = input("Enter your next move: ")
    while True:

        try:
            x_move, y_move = pos.split(" ", 1)
        except ValueError:
            print(invalid_pos)
            continue

        if x_move.isnumeric() == False or y_move.isnumeric() == False:
            print(invalid_pos, "num")
            pos = input("Invalid move! Enter your next move: ")
            continue
        elif len(pos.split(" ")) != 2:
            print(invalid_pos, "split err")
            pos = input("Invalid move! Enter your next move: ")
            continue
        elif int(x_move) not in range(1, a + 1) or int(y_move) not in range(1, b + 1):
            print(invalid_pos, "range 1 - b")
            pos = input("Invalid move! Enter your next move: ")
            continue
        else:
            x_move, y_move = int(x_move) - 1, b - int(y_move)
            #print(f"x: {x} y: {y}")
            #print(f"x: {x_move} y: {y_move}")
            for i in range(8):
                if y + moves[i][0] == y_move and x + moves[i][1] == x_move and y + moves[i][0] <= b and y + moves[i][0] >= 0 and x + moves[i][1] <= a and x + moves[i][1] >= 0 and board[y_move][x_move] != "X":
                    #print(f"x: {x} y: {y}")
                    #print(f"x: {x_move} y: {y_move}")
                    board[y_move][x_move] = "X"
                    print()
                    board[y][x] = "*"


                    return x_move, y_move

        pos = input("Invalid move! Enter your next move: ")

def board_clean():
    for i in range(b):
        for j in range(a):
            if board[i][j] in ["0", "1", "2", "3", "4", "5", "6", "7", "8"]:
                board[i][j] = "_"




#starting setup

#errors
invalid_dim = "Invalid dimensions!"
invalid_pos = "Invalid position!"

#getting board dimensions and knight's starting position, marking knight with X
a, b = ask_board()
global x
global y
x, y = ask_pos()
cell = len(str(b)) + 1  # calculates cell width for drawing board
board = [["_" for i in range(a)] for j in range(b)]

#default board state
board[y][x] = "X"

squares = 1
available_moves = 0

while True:
    board_clean()
    available_moves = check_moves()
    print(f"squares: {squares}")
    if available_moves == 0:
        if squares == a * b:
            print("What a great tour! Congratulations!")
            break
        else:
            print("No more possible moves!")
            print(f"Your knight visited {squares} squares!")
            break
    else:
        squares += 1
    x, y = ask_move()

