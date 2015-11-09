import csv
import os
from Tkinter import *
import tkSimpleDialog
import tkMessageBox

student_grades = {}
grade_prompt = 'Please enter a student name and score between 0 and 100 separated by a space: '
menu_prompt = ('1. Create the gradebook \n'
       '2. Read the gradebook \n'
       '3. Update the gradebook \n'
       '4. Delete the gradebook record \n'
       '5. Quite the gradebook \n'
       'Please choose a one of the options above: ')

if os.path.exists('student_score.txt') == True:
    with open('student_score.txt') as fh:
        for line in csv.reader(fh):
            student_grades[line[0]] = int(line[1])
else:
    pass
def write_file(grades):
    with open("student_score.txt", 'wb') as th:
        for key, value in grades.items():
            th.write(key + ',' + str(value) + '\n')

def create_grade():
    name = tkSimpleDialog.askstring("Create an Entry", "Please enter the student's name")
    name = name.capitalize()
    if name in student_grades:
        tkMessageBox.showinfo("Sorry", "Student already exists. Please choose a different option !!!")
    else:
        score = tkSimpleDialog.askstring("Create an Entry", "Please enter the student's score")
        if int(score) not in range(0, 101):
            tkMessageBox.showinfo("Sorry", "Only score from 0 to 100 is acceptable. Please do it again !!!")
        else:
            student_grades[name] = int(score)
            tkMessageBox.showinfo("Congratulation", "You created the grade book successfully")

def read_grade():
    read_name = tkSimpleDialog.askstring("Check The Grade", "Please put the name you want to check out the grade: ")
    read_name = read_name.capitalize()
    if read_name in student_grades:
        if student_grades[read_name] >= 90:
            tkMessageBox.showinfo("Result", "{0} {1}  A".format(read_name, student_grades[read_name]))
        elif student_grades[read_name] >= 80:
            tkMessageBox.showinfo("Result", "{0} {1}  B".format(read_name, student_grades[read_name]))
        elif student_grades[read_name] >=  70:
            tkMessageBox.showinfo("Result", "{0} {1}  C".format(read_name, student_grades[read_name]))
        elif student_grades[read_name] >= 60:
            tkMessageBox.showinfo("Result", "{0} {1}  D".format(read_name, student_grades[read_name]))
        elif student_grades[read_name] < 60:
            tkMessageBox.showinfo("Result", "{0} {1}  C".format(read_name, student_grades[read_name]))
    else:
        tkMessageBox.showinfo("Sorry", "The name you entered is not in the gradebook. Please do it again !!!")

def update_grade():
    update_name = tkSimpleDialog.askstring("Name to update", "Please enter the student you want to update: ")
    update_name = update_name.capitalize()
    if update_name not in student_grades:
        tkMessageBox.showinfo("Sorry", "The student you chose is not in the gradebook. Please enter a different name !!!")
    else:
        update_score = tkSimpleDialog.askinteger("Score to update", "Please enter the new score")
        if int(update_score) not in range(0, 101):
            tkMessageBox.showinfo("Sorry", "Only score from 0 to 100 is acceptable. Please do it again !!!")
        else:
            student_grades[update_name] = int(update_score)
            tkMessageBox.showinfo("Congratulation", "The student you chose has been updated ")

def del_grade():
    del_student = tkSimpleDialog.askstring("Delete a Student", "Please enter name of the student you want to delete.")
    del_student = del_student.capitalize()
    if del_student in student_grades:
        student_grades.pop(del_student)
        tkMessageBox.showinfo("Congratulation", "The student you chose has been deleted")
    else:
         tkMessageBox.showinfo("Sorry", "The student you chose is not in the gradebook")

def save_and_write():
    write_file(student_grades)
    tkMessageBox.showinfo("Ok", "Have a good day")
    exit()

def grade_book_program():
    while True:
        command = int(raw_input(menu_prompt).strip())
        if command > 5 or command < 1:
            print "Wrong input, please enter a number between 1 and 5"
        elif command == 1:
            update_grade()
        elif command == 2:
            read_grade()
        elif command == 3:
            update_grade()
        elif command == 4:
            del_grade()
        elif command == 5:
            save_and_write()

def create_a_gui():
    root = Tk()
    root.title("Gradebook Application")
    root.geometry("1080x500")

    frame = Frame(root)
    frame.pack()

    button_create = Button(frame, text = "Create a gradebook", command = create_grade, height=1, width=20, background="grey")
    button_read = Button(frame, text = "Read the gradebook", command = read_grade, height=1, width=20, background="blue")
    button_update = Button(frame, text = "Update the gradebook", command = update_grade, height=1, width=20, background="pink")
    button_delete = Button(frame, text = "Delete the gradebook", command = del_grade, height=1, width=20, background="purple")
    button_save = Button(frame, text = "Good Bye the gradebook", command = save_and_write, height=1, width=20, background="green")

    button_create.pack(side = TOP)
    button_read.pack(side = TOP)
    button_update.pack(side = TOP)
    button_delete.pack(side = TOP)
    button_save.pack(side = TOP)

    root.mainloop()

create_a_gui()