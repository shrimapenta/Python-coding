numbers = []

for i in range(3):
    row = []

    for j in range(3):
        number = int(input("Enter a number: "))
        row.append(number)

    numbers.append(row)

total = 0

for i in range(3):
    for j in range(3):
        total = total + numbers[i][j]

average = total / 9

print("Sum:", total)
print("Average:", average)