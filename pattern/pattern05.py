numOfRows = int(input("Enter the number of rows: "))

isSolved = True
goingReverse = False

currentRow = 1

while isSolved:
    print("*" * currentRow)

    if currentRow < numOfRows and not goingReverse:
        currentRow = currentRow + 1

    elif currentRow == numOfRows:
        goingReverse = True
        currentRow = currentRow - 1

    else:
        currentRow = currentRow - 1

    if currentRow == 0 and goingReverse:
        isSolved = False
