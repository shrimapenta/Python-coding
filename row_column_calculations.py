numbers = []

for i in range(3):
    row = []

    for j in range(3):
        number = int(input("Enter a number: "))
        row.append(number)

    numbers.append(row)

for j in range(3):
    total = 0

    for i in range(3):
        total = total + numbers[i][j]

    print("Column", j + 1, "sum:", total)

for i in range(3):
    total = 0

    for j in range(3):
        total = total + numbers[i][j]

    print("Row", i + 1, "average:", total / 3)