names = []

for i in range(5):
    name = input("Enter a name: ")
    names.append(name)

reverse_names = []

for i in range(4, -1, -1):
    reverse_names.append(names[i])

print(reverse_names)