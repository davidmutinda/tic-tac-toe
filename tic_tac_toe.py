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