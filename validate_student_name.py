student = "Bob"

def changeOfName():
    global student

    new_name = input("Enter the new name: ")

    if new_name != student:
        student = new_name
    else:
        print("The new name is not different.")

    print("Current name:", student)

changeOfName()