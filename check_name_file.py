import os

if os.path.exists("name.txt"):
    file = open("name.txt", "r")
    name = file.readline()
    file.close()

    print("Hello", name)
else:
    name = input("What is your name? ")

    print("Hello", name)

    file = open("name.txt", "w")
    file.write(name)
    file.close()