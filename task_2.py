def chess_board(n,k):
    for i in range(n):
        for j in range(k):
            print((' '*k+'#'*k)*k)
        for j in range(k):
            print(('#'*k+' '*k)*k)
