def gameplay(value):
    """This function takes the position the player inputs and prints  it on the grid"""
    steps = [
        (0,0),
        (0,1),
        (0,2),
        (1,0),
        (1,1),
        (1,2),
        (2,0),
        (2,1),
        (2,2)
    ]
    
    try:
        a = int(input("Choose a position (1 - 9): "))
    except:
        print("\033[91mInput integer values only!! \033[0m")
        return "fail"
    if a < 1 or a > 9:
        print("\033[91mInput a number between 1 and 9!! \033[0m")
        return "fail"
    b = 1
    for (i, j) in steps:
        if a == b:
            break
        b += 1

    if arr[i][j] != ' ':
        print("\033[91mSpot occupied! Choose another position \033[0m")
        return "fail"
    arr[i][j] = value

    
    print(f'\033[93m{arr[0][0]} | {arr[0][1]} | {arr[0][2]}') 
    print("---------")
    print(f'{arr[1][0]} | {arr[1][1]} | {arr[1][2]}') 
    print("---------")
    print(f'{arr[2][0]} | {arr[2][1]} | {arr[2][2]}')
    print("\033[0m")

def player1():
    """This function is the entry point and allows player 1 to play it"""
    c = 0
    d = 0
    for c in range(0,3):
        for d in range(0,3):
            if arr[c][d] == " ":
                break
        if arr[c][d] == " ":
            break 
    if c == 2 and d == 2:
        print("\033[32mDraw!! \033[0m")
        print(" ")
        print("\033[91mGame over!!")
        print("\033[0m")
        quit()

    print("\033[91mPLAYER 1's turn \033[0m")
    result = "fail"
    while result == "fail":
        result = gameplay('x')
    winner = checkWinner()
    if winner == "yes":
        print("\033[32mPlayer 1 won!!! \033[0m")
        return
    player2()

arr = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
winner = " "
print("\033[32mWELCOME TO SHELBYS' TICTACTOE GAME")
print("----------------------------------")
print("Player 1 character = x")
print("Player 2 character = 0 \033[0m")
print(" ")
print(f'\033[93m{arr[0][0]} | {arr[0][1]} | {arr[0][2]}') 
print("---------")
print(f'{arr[1][0]} | {arr[1][1]} | {arr[1][2]}') 
print("---------")
print(f'{arr[2][0]} | {arr[2][1]} | {arr[2][2]}')
print("\033[0m")
player1()