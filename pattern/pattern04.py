numOfRows = int(input("Enter the number fo rows: "))

for i in range(1, numOfRows + 1):
    for j in range(1, i + 1):
        print(str(j), end=" ")
        if j == i:
            print()
