#!/usr/bin/python3
# Define a class to represent individual student records
class Student:
    def __init__(self, student_id, name, age, gpa):
        # Initialize attributes for student ID, name, age, GPA
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gpa = gpa
        # Initialize next attribute to None (no next node initially)
        self.next = None

# Define a class to manage the collection of student records using a linked list
class StudentDatabase:
    def __init__(self):
        # Initialize head attribute to None (empty linked list initially)
        self.head = None
    
    # Method to add a new student record to the linked list
    def add_student(self, student_id, name, age, gpa):
        # Create a new Student object with the provided data
        new_student = Student(student_id, name, age, gpa)
        # If the linked list is empty, set the new student as the head
        if not self.head:
            self.head = new_student
        else:
            # Traverse the linked list to find the last node
            current = self.head
            while current.next:
                current = current.next
            # Add the new student as the next node of the last node
            current.next = new_student
    
    # Method to display all student records in the linked list
    def display_students(self):
        # Start traversal from the head of the linked list
        current = self.head
        # Traverse the linked list and print each student's information
        while current:
            print(f"Student ID: {current.student_id}, Name: {current.name}, Age: {current.age}, GPA: {current.gpa}")
            # Move to the next node
            current = current.next

# Example Usage:
# Create a new StudentDatabase object
student_db = StudentDatabase()
# Add student records to the database
student_db.add_student(101, "Alice", 20, 3.5)
student_db.add_student(102, "Bob", 21, 3.8)
student_db.add_student(103, "Charlie", 19, 3.2)
# Display all student records in the database
student_db.display_students()

