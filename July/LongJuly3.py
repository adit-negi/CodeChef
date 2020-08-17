T = input()
t = int(T)
for i in range(t):
    K = input()
    n = int(K)
    chessBoard = [["X" for i in range(8)] for j in range(8)]
    chessBoard[0][0] = "O"
    for i in range(8):
        for j in range(8):
            if n > 0 and n < 65:
                chessBoard[i][j] = "."
                n = n-1
            if n == 0:
                break

    chessBoard[0][0] = "O"
    for i in range(8):
        for j in range(8):
            print(chessBoard[i][j], end="")
        print()
