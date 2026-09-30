import random

numbers = []

for i in range(3):
    row = []

    for j in range(3):
        row.append(random.randint(1, 10))

    numbers.append(row)

for row in numbers:
    print(row)

principal = 0
secondary = 0

for i in range(3):
    principal = principal + numbers[i][i]
    secondary = secondary + numbers[i][2 - i]

print("Principal diagonal:", principal)
print("Secondary diagonal:", secondary)