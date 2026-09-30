numbers = [10, 20, 30]

numbers.append(40)
numbers.append(50)
numbers.append(60)

print(len(numbers))
print(numbers[0])

first = numbers[0]

for i in range(1, len(numbers)):
    numbers[i] = first

print(numbers)