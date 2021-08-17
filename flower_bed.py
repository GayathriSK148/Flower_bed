N = input("Enter a number between 1 and 26: ")
def flower_bed(N):
    N = int(N)
    low = 0
    high = 2*N - 1
    alp = {}
    value = N
    for i in range(1, 27):
        alp[i] = chr(ord('@')+ i)
    matrix = [[0 for x in range(2*N)]for y in range(2*N)]
    for i in range(N):
        for j in range(low, high+1):
            matrix[i][j] = alp[value]
        for j in range(low+1, high+1):
            matrix[j][i] = alp[value]
        for j in range(low+1, high+1):
            matrix[high][j] = alp[value]
        for j in range(low+1, high):
            matrix[j][high] = alp[value]

        low = low+1
        high = high-1
        value = value-1

    for a in range (2*N):
        for b in range(2*N):
            print(matrix[a][b], end = " ")
        print()

flower_bed(N)
