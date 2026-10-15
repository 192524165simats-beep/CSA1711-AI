board = [' '] * 9

for i in range(9):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])

    pos = int(input("Enter position (1-9): ")) - 1
    if board[pos] == ' ':
        board[pos] = 'X' if i % 2 == 0 else 'O'
    else:
        print("Position occupied!")
        continue

    for a, b, c in [(0,1,2),(3,4,5),(6,7,8),
                    (0,3,6),(1,4,7),(2,5,8),
                    (0,4,8),(2,4,6)]:
        if board[a] == board[b] == board[c] != ' ':
            print(board)
            print(board[a], "wins!")
            quit()

print("Game draw!")
