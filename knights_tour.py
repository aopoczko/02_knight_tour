'''
board row <- b ->
board col a
knight pos row <- y ->
knight pos col x
'''
def draw_board(a, b):
    #print("a :", a, ", b: ", b)
    #print(" " * (cell - 1), "-" * ((cell + 1) * a), "---", sep = "")
    print(" " * (cell - 1), "-" * ((len(str(a * b)) + 1) * a), "---", sep="")

    for i in range(b):
        #print("".join([str(b - i).rjust(cell - 1), "|"]))
        print("".join([str(b - i).rjust(cell - 1), "|"]), " ".join([board[i][j].rjust(len(str(a * b)), "_") if board[i][j] != "X" else board[i][j].rjust(len(str(a * b)))  for j in range(a)]), "|")
        #print(" ".join(board[i]).rjust(cell, "_"))
        #print(i)
        #print("".join([str(b - i).rjust(cell - 1), "|"]), " ".join([(board[i][j].rjust(cell, "_")) for j in range(a)]), "|")

    print(" " * (cell - 1), "-" * ((len(str(a * b)) + 1) * a), "---", sep = "")
    print(" " * (len(str(a)) +1), " ".join([(str(r+1).rjust(len(str(a * b)))) for r in range(a)]))
    #print(" ".join(["_" * len(str(a*b)) for _ in range(b)]))

invalid_dim = "Invalid dimensions!"
invalid_pos = "Invalid position!"

a, b = "", ""

while True:
    dim = input("Enter your board dimensions: ")
    try:
        a, b = dim.split(" ", 1)
    except ValueError:
        print(invalid_dim)

    if a.isnumeric() == False or b.isnumeric() == False:
        print(invalid_dim)
        continue
    elif len(dim.split(" ")) != 2:
        print(invalid_dim)
        continue
    elif int(a) < 0 or int(b) < 0:
        print(invalid_dim)
        continue
    else:
        break

a = int(a)
b = int(b)

board = [["_" for i in range(a)] for j in range(b)]

cell = len(str(b)) + 1
pos = input("Enter the knight's starting position: ")
x, y = "", ""

try:
    x, y = pos.split(" ", 1)
except ValueError:
    print(invalid_pos)

if x.isnumeric() == False or y.isnumeric() == False:
    print(invalid_pos, "num")
elif len(pos.split(" ")) != 2:
    print(invalid_pos, "split err")
elif int(x) not in range(1, a + 1) or int(y) not in range(1, b + 1):
    print(invalid_pos, "range 1 - b")
else:
    #print("a-y: ", (a - int(y)), " x-1: ", (int(x) - 1))
    #print("kon x: ", x, "y: ", y)
    board[b - int(y)][int(x) - 1] = "X"
    draw_board(a, b)

