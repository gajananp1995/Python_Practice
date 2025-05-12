# Creating a dictionary with student names as keys and their marks as values
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "David": 74,
    "Emma": 88
}

# Asking the user for a student's name
student_name = input("Enter the student's name: ")

# Retrieving and displaying the corresponding marks
if student_name in student_marks:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print(f"Error: student not found '{student_name}'")
