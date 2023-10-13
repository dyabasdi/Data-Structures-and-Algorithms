import math
HW_ERROR_MESSAGE = "   Grade must be in range [0..10]. Try again."
PR_EX_ERROR_MESSAGE = "   Grade must be in range [0..100]. Try again."
def receiveName():
    studentName = input("Enter the student/'s name (or /'stop/'): ")
    if studentName == "stop":
        print("Thanks for using the grade calculator! Goodbye.")
        quit()
    return studentName
def compHW():
    print()
    print("HOMEWORKS:")
    hw1grade = -1
    while hw1grade < 0 or hw1grade > 10:
        hw1grade = int(input("   Enter HW1 grade: "))
        if hw1grade < 0 or hw1grade > 10:
            print (HW_ERROR_MESSAGE)
    hw2grade = -1
    while hw2grade < 0 or hw2grade > 10:
        hw2grade = int(input("   Enter HW2 grade: "))
        if hw2grade < 0 or hw2grade > 10:
            print (HW_ERROR_MESSAGE)
    hw3grade = -1
    while hw3grade < 0 or hw3grade > 10:
        hw3grade = int(input("   Enter HW3 grade: "))
        if hw3grade < 0 or hw3grade > 10:
            print (HW_ERROR_MESSAGE)
    hwAvg = float((hw1grade + hw2grade + hw3grade)/.3)
    return hwAvg
def compProj():
    print()
    print("PROJECTS:")
    proj1 = -1
    while proj1 < 0 or proj1 > 100:
        proj1 = int(input("   Enter Pr1 grade: "))
        if proj1 < 0 or proj1 > 100:
            print (PR_EX_ERROR_MESSAGE)
    proj2 = -1
    while proj2 < 0 or proj2 > 100:
        proj2 = int(input("   Enter Pr2 grade: "))
        if proj2 < 0 or proj2 > 100:
            print (PR_EX_ERROR_MESSAGE)
    prAvg = float((proj1 + proj2)/2)
    return prAvg
def compExam():
    print()
    print("EXAMS:")
    ex1 = -1
    while ex1 < 0 or ex1 > 100:
        ex1 = int(input("   Enter Ex1 grade: "))
        if ex1 < 0 or ex1 > 100:
            print (PR_EX_ERROR_MESSAGE)
    ex2 = -1
    while ex2 < 0 or ex2 > 100:
        ex2 = int(input("   Enter Ex2 grade: "))
        if ex2 < 0 or ex2 > 100:
            print (PR_EX_ERROR_MESSAGE)
    exAvg = float((ex1 + ex2)/2)
    return exAvg
def gradeReport(studentName, hwAvg, prAvg, exAvg):
    print()
    print("Grade report for:", studentName)
    print("   Homework average (30% of grade):", format(hwAvg, ".2f"))
    print("   Project average (30% of grade):", format(prAvg, ".2f"))
    print("   Exam average (40% of grade):", format(exAvg, ".2f"))
    studentAvg = (hwAvg*.3)+(prAvg*.3)+(exAvg*.4)
    print("   Student course average:", format(studentAvg, ".2f"))
    if studentAvg < 60:
        print("   Course grade (CS303E: Fall, 2022): F")
    elif studentAvg >= 60 and studentAvg < 70:
        print("   Course grade (CS303E: Fall, 2022): D")
    elif studentAvg >= 70 and studentAvg < 80:
        print("   Course grade (CS303E: Fall, 2022): C")
    elif studentAvg >= 80 and studentAvg < 90:
        print("   Course grade (CS303E: Fall, 2022): B")
    elif studentAvg >= 90:
        print("   Course grade (CS303E: Fall, 2022): A")

studentName = receiveName()
hwAvg = compHW()
prAvg = compProj()
exAvg = compExam()
gradeReport(studentName, hwAvg, prAvg, exAvg)





    
