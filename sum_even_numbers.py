total = 0

for i in range(10):
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        total = total + number

print(total)