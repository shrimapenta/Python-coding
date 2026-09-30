numbers = []

for i in range(6):
    number = int(input("Enter a number: "))
    numbers.append(number)

if numbers[0] == numbers[5]:
    print(True)
else:
    print(False)