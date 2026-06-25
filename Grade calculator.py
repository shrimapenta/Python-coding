marks1=int(input("Enter your marks in English: "))
marks2=int(input("Enter your marks in Math: "))
marks3=int(input("Enter your marks in Science: "))

def marks_total():
    return marks1+marks2+marks3
total=marks_total()
print("Total marks = ",total)

def marks_average():
    return total/3
average=marks_average()
print("Average score = ",average)

def grade_check():
    if 90<= average <=100:
        print("Grade A")
    elif 75 <= average <= 89:
        print("Grade B")
    elif 50 <= average <= 74:
        print("Grade C")
    elif 35 <= average <= 49:
        print("Grade D")
    else:
        print("Fail")
grade_check()