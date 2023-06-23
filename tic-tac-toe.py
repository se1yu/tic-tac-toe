first = [1,2,3]
second = [4,5,6]
third = [7,8,9]
grid = []
grid.append(first)
grid.append(second)
grid.append(third)
# to call a row in grid, do grid[INDEX OF ROW])
# for example. grid[1]) == [4,5,6]
turns = [1,2,3,4,5,6,7,8,9]
print("Welcome to tic-tac-toe!\nThere will be two users playing.")
input("Press enter to continue. ")
print("\n\n\n\n")
 
print("Player 1 will be X, and player 2 will be O.\nEnter a number 1-9 to choose a location to mark as shown below.")
player1 = input('Player 1...Please enter your name: ')
player2 = input('Player 2...Please enter your name: ')
endgame = False
print("\nWelcome,", player1, "and", player2+"!") 
while turns != []:
    hor_row_check = []
    hor = 0
    for i in grid:
        print(str(i))
        #prints all numbers in 3 seperate lines
    
    if len(turns) % 2 != 0: 
        current_player = player1
    else:
        current_player = player2
    print("\n\n")

    check = int(input(current_player+", enter a # to place on the grid: "))
    print()

    '''
    if check.isalpha:
        if check== "R":
            continue
    elif check.isdigit:
        check = int(check)
    '''
    while not check in turns: # will repeat til valid num
        print("Please choose a NEW number between 1-9.")
        check = int(input(current_player,"enter #: "))
    
    else:
        turns.remove(check)
        #print("These are turns",turns) 
        #it works, removes the user selected number from 'turns' list

    for row in grid: #for a row in the grid
        if check in row: #if selected num in that row then 
            # print(check, "in", i) it works YESS
            indx = (check % 3) - 1 #index of NUMBER'S POSITION IN ROW OF GRID.


           # print("index is",indx)
            if current_player == player2:
                row[indx] = "O"
            else:
                row[indx] = "X" 
    # ---- establishing columns in the grid
    column1 = []
    for i in range(3):

        column1.append(grid[i][0]) #do grid [i] [i] for diagonal (1 5 9)
    column2 = []
    for i in range(3):
        column2.append(grid[i][1])
    column3 = []
    for i in range(3):
        column3.append(grid[i][2])
    # --- establishing the 2 diagonals in grid
    diag1 = []
    y = 0
    for i in range(2,-1,-1): 
        diag1.append(grid[i][y])
        y+= 1
    diag2 = []
    for i in range(3):
        diag2.append(grid[i][i])
    ########################################33
    for row in grid:
        if row == ['X','X','X'] or column1 == ['X','X','X'] or column2 == ['X','X','X'] or column3 == ['X','X','X'] or diag1 == ['X','X','X'] or diag2 == ['X','X','X']:
            print()
            print(player1, "wins!")
            endgame = True
            break
        elif row == ['O','O','O'] or column1 == ['O','O','O'] or column2 == ['O','O','O'] or column3 == ['O','O','O'] or diag2 == ['O','O','O'] or diag1 == ['O','O','O']: 
            print(player2, "wins!")
            endgame= True
            break
    if endgame:
        break
print()
for row in grid:
    print(row)

if turns == [] and not endgame:
    print("The game is tied!")

## --- notes --- ##
# find out how to make TTT grid not expand