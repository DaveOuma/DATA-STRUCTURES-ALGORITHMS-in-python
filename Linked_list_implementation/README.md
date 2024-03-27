# Linked List Implementation in Python

Linked lists are fundamental data structures in computer science and programming. Unlike arrays, which store elements in contiguous memory locations, linked lists consist of nodes connected by pointers, allowing for dynamic memory allocation and flexible data storage. Each node in a linked list contains data and a reference to the next node in the sequence, forming a chain-like structure.

## Node Class with Data and Next Attributes:

We define a `Node` class to represent each element in a linked list. Each node has two attributes: `data`, which stores the value of the element, and `next`, which points to the next node in the sequence.

## Methods for Insertion, Deletion, and Traversal:

To interact with linked lists, we need to implement methods for inserting new nodes, deleting existing nodes, and traversing the list to access or modify its elements. Insertion methods allow us to add new nodes at the beginning, end, or middle of the list. Deletion methods enable us to remove nodes based on their position or value. Traversal methods facilitate the iteration through the list to access each node's data sequentially.

## Example:

Suppose we are managing a database of student records and need to store information such as student ID, name, age, and GPA. We can use a linked list to efficiently organize and manage this data.

```python
class Student:
    def __init__(self, student_id, name, age, gpa):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.gpa = gpa
        self.next = None

class StudentDatabase:
    def __init__(self):
        self.head = None
    
    def add_student(self, student_id, name, age, gpa):
        new_student = Student(student_id, name, age, gpa)
        if not self.head:
            self.head = new_student
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_student
    
    def display_students(self):
        current = self.head
        while current:
            print(f"Student ID: {current.student_id}, Name: {current.name}, Age: {current.age}, GPA: {current.gpa}")
            current = current.next

# Example Usage:
student_db = StudentDatabase()
student_db.add_student(101, "Alice", 20, 3.5)
student_db.add_student(102, "Bob", 21, 3.8)
student_db.add_student(103, "Charlie", 19, 3.2)
student_db.display_students()

"""In this example, we define a Student class to represent individual student records, with attributes for student ID, name, age, GPA, and a next pointer to connect nodes in the linked list. Then, we create a StudentDatabase class to manage the collection of student records using a linked list. The add_student method inserts new student records at the end of the list, and the display_students method traverses the list to print each student's information. This linked list implementation provides an efficient way to store and retrieve student data in our database."""
