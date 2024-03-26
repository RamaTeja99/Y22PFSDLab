class Student:
  def __init__(self, student_id, student_name):
    self.student_id = student_id
    self.student_name = student_name

# Create a student object
student1 = Student(input('Enter the student id number:\n'), input('Enter the student name:\n'))

# Add a new attribute
student1.student_class = input('Enter the Student Class Number:\n')

# Display all attributes and their values
print("**Before removing student_name:**")
print(f"Student ID: {student1.student_id}")
print(f"Student Name: {student1.student_name}")
print(f"Student Class: {student1.student_class}")

# Remove the student_name attribute
del student1.student_name

# Display remaining attributes and their values
print("\n**After removing student_name:**")
print(f"Student ID: {student1.student_id}")
print(f"Student Class: {student1.student_class}")