numOfRows = int(input("Enter the number of rows: "))
maxNumOFStarsEachRow = (numOfRows * 2) - 1

isValid = True
goingReverse = False

startingIndex = 1
endingIndex = maxNumOFStarsEachRow

currentRow = numOfRows

while isValid:
    currentOuterRow = numOfRows
    currentString = ""

    for i in range(1, maxNumOFStarsEachRow + 1):
        if startingIndex <= i <= endingIndex:
            currentString = currentString + str(currentRow)

        else:
            currentString = currentString + str(currentOuterRow)

        if i < startingIndex - 1:
            currentOuterRow = currentOuterRow - 1

        elif i > endingIndex:
            currentOuterRow = currentOuterRow + 1

    print(currentString)

    if currentRow > 1 and not goingReverse:
        currentRow = currentRow - 1
        startingIndex = startingIndex + 1
        endingIndex = endingIndex - 1

    else:
        goingReverse = True
        currentRow = currentRow + 1
        startingIndex = startingIndex - 1
        endingIndex = endingIndex + 1

    if currentRow == numOfRows + 1 and goingReverse:
        isValid = False
