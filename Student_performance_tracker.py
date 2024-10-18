# Step 1: Creating the Student class
class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.grades = {}  # Dictionary to store subjects and grades

    def add_grade(self, subject, grade):
        if 0 <= grade <= 100:
            self.grades[subject] = grade
        else:
            print("Invalid grade. Please enter a grade between 0 and 100.")

    def calculate_average(self):
        if self.grades:
            total = sum(self.grades.values())
            return total / len(self.grades)
        else:
            return 0

    def display_info(self):
        print(f"Student Name: {self.name}, Roll Number: {self.roll_number}")
        print("Grades:")
        for subject, grade in self.grades.items():
            print(f"{subject}: {grade}")
        print(f"Average Grade: {self.calculate_average():.2f}")


# Step 2: Creating the StudentTracker class
class StudentTracker:
    def __init__(self):
        self.students = {}  # Dictionary to store students by roll number

    def add_student(self, name, roll_number):
        if roll_number not in self.students:
            student = Student(name, roll_number)
            self.students[roll_number] = student
            print(f"Student {name} added successfully.")
        else:
            print("A student with this roll number already exists.")

    def add_grades(self, roll_number, subject, grade):
        if roll_number in self.students:
            student = self.students[roll_number]
            student.add_grade(subject, grade)
        else:
            print("Student not found.")

    def view_student_details(self, roll_number):
        if roll_number in self.students:
            student = self.students[roll_number]
            student.display_info()
        else:
            print("Student not found.")

    def calculate_student_average(self, roll_number):
        if roll_number in self.students:
            student = self.students[roll_number]
            return student.calculate_average()
        else:
            print("Student not found.")


# Step 3: Adding User Interaction
def main_menu():
    tracker = StudentTracker()

    while True:
        print("\n--- Student Performance Tracker ---")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student Details")
        print("4. Calculate Student Average")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            name = input("Enter student name: ").strip()
            roll_number = input("Enter roll number: ").strip()
            tracker.add_student(name, roll_number)

        elif choice == '2':
            roll_number = input("Enter student roll number: ").strip()
            subject = input("Enter subject: ").strip()
            try:
                grade = float(input("Enter grade (0-100): ").strip())
                tracker.add_grades(roll_number, subject, grade)
            except ValueError:
                print("Please enter a valid grade.")

        elif choice == '3':
            roll_number = input("Enter student roll number: ").strip()
            tracker.view_student_details(roll_number)

        elif choice == '4':
            roll_number = input("Enter student roll number: ").strip()
            avg = tracker.calculate_student_average(roll_number)
            if avg is not None:
                print(f"Average grade: {avg:.2f}")

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main_menu()
