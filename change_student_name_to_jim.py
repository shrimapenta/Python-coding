student = "Bob"

def changeOfName():
    global student
    student = "Jim"
    print("Student inside the method:", student)

changeOfName()
print("Student outside the method:", student)