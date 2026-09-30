size = int(input("Enter the size of the array: "))

numbers = []

for i in range(size):
    number = int(input("Enter a number: "))
    numbers.append(number)

even_sum = 0
odd_count = 0
total = 0

for number in numbers:
    total = total + number

    if number % 2 == 0:
        even_sum = even_sum + number
    else:
        odd_count = odd_count + 1

average = total / size

print("Sum of even numbers:", even_sum)
print("Average:", average)
print("Number of odd numbers:", odd_count)