"""
Student Management System - Mini Project
Features: Add, View, Search, Update, Delete students
Data is saved in students.json (so it stays after you close the program)
Run: python student_management.py
"""

import json
import os

FILE_NAME = "students.json"


# ---------- File handling ----------
def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []


def save_students(students):
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)


# ---------- Helpers ----------
def find_student(students, roll):
    for s in students:
        if s["roll"] == roll:
            return s
    return None


def get_marks(prompt):
    while True:
        try:
            marks = float(input(prompt))
            if 0 <= marks <= 100:
                return marks
            print("Marks must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")


def get_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 75:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 50:
        return "C"
    elif marks >= 35:
        return "D"
    return "F"


def print_student(s):
    print(f"Roll No : {s['roll']}")
    print(f"Name    : {s['name']}")
    print(f"Age     : {s['age']}")
    print(f"Course  : {s['course']}")
    print(f"Marks   : {s['marks']}  (Grade: {get_grade(s['marks'])})")
    print("-" * 30)


# ---------- Features ----------
def add_student(students):
    print("\n--- Add Student ---")
    roll = input("Roll number: ").strip()
    if not roll:
        print("Roll number cannot be empty.")
        return
    if find_student(students, roll):
        print("A student with this roll number already exists!")
        return

    name = input("Name: ").strip()
    try:
        age = int(input("Age: "))
    except ValueError:
        print("Invalid age.")
        return
    course = input("Course: ").strip()
    marks = get_marks("Marks (0-100): ")

    students.append(
        {"roll": roll, "name": name, "age": age, "course": course, "marks": marks}
    )
    save_students(students)
    print("Student added successfully!")


def view_students(students):
    print("\n--- All Students ---")
    if not students:
        print("No records found.")
        return
    for s in students:
        print_student(s)
    print(f"Total students: {len(students)}")


def search_student(students):
    print("\n--- Search Student ---")
    keyword = input("Enter roll number or name: ").strip().lower()
    results = [
        s for s in students
        if keyword == s["roll"].lower() or keyword in s["name"].lower()
    ]
    if not results:
        print("No student found.")
        return
    for s in results:
        print_student(s)


def update_student(students):
    print("\n--- Update Student ---")
    roll = input("Enter roll number to update: ").strip()
    s = find_student(students, roll)
    if not s:
        print("Student not found.")
        return

    print("Leave blank to keep the current value.")
    name = input(f"Name [{s['name']}]: ").strip()
    age = input(f"Age [{s['age']}]: ").strip()
    course = input(f"Course [{s['course']}]: ").strip()
    marks = input(f"Marks [{s['marks']}]: ").strip()

    if name:
        s["name"] = name
    if age:
        try:
            s["age"] = int(age)
        except ValueError:
            print("Invalid age, keeping old value.")
    if course:
        s["course"] = course
    if marks:
        try:
            m = float(marks)
            if 0 <= m <= 100:
                s["marks"] = m
            else:
                print("Marks out of range, keeping old value.")
        except ValueError:
            print("Invalid marks, keeping old value.")

    save_students(students)
    print("Student updated successfully!")


def delete_student(students):
    print("\n--- Delete Student ---")
    roll = input("Enter roll number to delete: ").strip()
    s = find_student(students, roll)
    if not s:
        print("Student not found.")
        return
    confirm = input(f"Delete {s['name']}? (y/n): ").lower()
    if confirm == "y":
        students.remove(s)
        save_students(students)
        print("Student deleted.")
    else:
        print("Cancelled.")


def show_topper(students):
    print("\n--- Topper ---")
    if not students:
        print("No records found.")
        return
    top = max(students, key=lambda x: x["marks"])
    print_student(top)


# ---------- Main menu ----------
def main():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Show Topper")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            show_topper(students)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
