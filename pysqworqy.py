board = ['-','-','-',
         '-','-','-',
         '-','-','-']

player = ''

def start_game():
    print("Piškvorky (Tic-tac-toe)")
    select_mark()
    draw_board()

    while True:
        while True:
            get_position()

            if board[0] == board[1] == board[2] != '-':
                print("Gratulace hráči " + board[2] + ", vyhrál jsi!")
                break
            elif board[3] == board[4] == board[5] != '-':
                print("Gratulace hráči " + board[5] + ", vyhrál jsi!")
                break
            elif board[6] == board[7] == board[8] != '-':
                print("Gratulace hráči " + board[8] + ", vyhrál jsi!")
                break
            elif board[0] == board[3] == board[6] != '-':
                print("Gratulace hráči " + board[6] + ", vyhrál jsi!")
                break
            elif board[1] == board[4] == board[7] != '-':
                print("Gratulace hráči " + board[7] + ", vyhrál jsi!")
                break
            elif board[2] == board[5] == board[8] != '-':
                print("Gratulace hráči " + board[8] + ", vyhrál jsi!")
                break
            elif board[0] == board[4] == board[8] != '-':
                print("Gratulace hráči " + board[8] + ", vyhrál jsi!")
                break
            elif board[2] == board[4] == board[6] != '-':
                print("Gratulace hráči " + board[6] + ", vyhrál jsi!")
                break
            elif '-' not in board:
                print("Remíza")
                break

        restart = input("Chceš hrát znovu? [A/N] ")
        while restart not in ['A', 'N']:
            print("Neplatný input")
            restart = input("Chceš hrát znovu? [A/N] ")

        if restart == 'N':
            break
        
        clear_board()
        draw_board()

def select_mark():
    print("Vyber si značku - X nebo O")

    global player

    player = input("Hráč 1: ")
    while player not in ['X', 'O']:
        print("Neplatný input, vyber X nebo O")
        player = input("Hráč 1: ")
    
    if player == 'X':
        print("Hráč 2: O")
        return

    print("Hráč 2: X")

def draw_board():
    print(board[0] + " | " + board[1] + " | " + board[2] + '\t' + "1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + '\t' + "4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + '\t' + "7 | 8 | 9")

def get_position():
    global player

    print("Teď hraje: " + player)

    while True:
        position = input("Vyber pozici od 1 do 9: ")
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Neplatný input")
            position = input("Vyber pozici od 1 do 9: ")
        position = int(position) - 1

        if board[position] != '-':
            print("Pozice už byla zabrána, vyber si jinou!")
            continue

        break

    board[position] = player
    draw_board()

    if player == 'X':
        player = 'O'
        return
    
    player = 'X'

def clear_board():
    global board
    board = ['-','-','-',
             '-','-','-',
             '-','-','-']

start_game()