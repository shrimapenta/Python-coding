import random

file = open("numb.txt", "w")

for i in range(100):
    number = random.randint(1, 70)
    file.write(str(number) + "\n")

file.close()