# Student Result Management System
# Author: Misha Kumari
# Internship Project

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        self.total = sum(marks.values())
        self.percentage = self.total / len(marks)

    def get_grade(self):
        if self.percentage >= 90:
            return "A+"
        elif self.percentage >= 75:
            return "A"
        elif self.percentage >= 60:
            return "B"
        elif self.percentage >= 40:
            return "C"
        else:
            return "Fail"

    def display_result(self):
        print(f"\nRoll No: {self.roll_no}")
        print(f"Name: {self.name}")
        print("Marks:")
        for subject, mark in self.marks.items():
            print(f"  {subject}: {mark}")
        print(f"Total Marks: {self.total}")
        print(f"Percentage: {self.percentage:.2f}%")
        print(f"Grade: {self.get_grade()}")


# Sample run
if __name__ == "__main__":
    print("---- Student Result Management System ----")
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")

    subjects = ["Maths", "Physics", "Chemistry", "English", "Computer"]
    marks = {}
    for subject in subjects:
        mark = int(input(f"Enter marks for {subject}: "))
        marks[subject] = mark

    student = Student(roll_no, name, marks)
    student.display_result()
