numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)

temp = numbers[1]
numbers[1] = numbers[2]
numbers[2] = temp

print(numbers)