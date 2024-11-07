import json


class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_person_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")


class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id
        self.grades = {}
        self.courses = []

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def enroll_course(self, course):
        self.courses.append(course)

    def display_student_info(self):
        print(f"Student Information:")
        print(f"Name: {self.name}")
        print(f"ID: {self.student_id}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")
        print(f"Enrolled Courses: {', '.join(self.courses)}")
        print(f"Grades: {self.grades}")


class Course:
    def __init__(self, course_name, course_code, instructor):
        self.course_name = course_name
        self.course_code = course_code
        self.instructor = instructor
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_course_info(self):
        print(f"Course Information:")
        print(f"Course Name: {self.course_name}")
        print(f"Course Code: {self.course_code}")
        print(f"Instructor: {self.instructor}")
        print(f"Enrolled Students: {', '.join([student.name for student in self.students])}")


class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.courses = {}

    def add_student(self, name, age, address, student_id):
        if student_id in self.students:
            print(f"Student with ID {student_id} already exists.")
        else:
            student = Student(name, age, address, student_id)
            self.students[student_id] = student
            print(f"Student {name} (ID: {student_id}) added successfully.")

    def add_course(self, course_name, course_code, instructor):
        if course_code in self.courses:
            print(f"Course with code {course_code} already exists.")
        else:
            course = Course(course_name, course_code, instructor)
            self.courses[course_code] = course
            print(f"Course {course_name} (Code: {course_code}) created with instructor {instructor}.")

    def enroll_student_in_course(self, student_id, course_code):
        if student_id not in self.students:
            print(f"Student with ID {student_id} does not exist.")
            return
        if course_code not in self.courses:
            print(f"Course with code {course_code} does not exist.")
            return

        student = self.students[student_id]
        course = self.courses[course_code]
        student.enroll_course(course.course_name)
        course.add_student(student)
        print(f"Student {student.name} (ID: {student_id}) enrolled in {course.course_name} (Code: {course_code}).")

    def add_grade(self, student_id, course_code, grade):
        if student_id not in self.students:
            print(f"Student with ID {student_id} does not exist.")
            return
        if course_code not in self.courses:
            print(f"Course with code {course_code} does not exist.")
            return

        student = self.students[student_id]
        if course_code not in student.courses:
            print(f"Student {student.name} is not enrolled in the course with code {course_code}.")
            return

        student.add_grade(course_code, grade)
        print(f"Grade {grade} added for {student.name} in {course_code}.")

    def display_student_details(self, student_id):
        if student_id not in self.students:
            print(f"Student with ID {student_id} does not exist.")
            return
        student = self.students[student_id]
        student.display_student_info()

    def display_course_details(self, course_code):
        if course_code not in self.courses:
            print(f"Course with code {course_code} does not exist.")
            return
        course = self.courses[course_code]
        course.display_course_info()

    def save_data(self, filename="data.json"):
        data = {
            "students": {student_id: student.__dict__ for student_id, student in self.students.items()},
            "courses": {course_code: course.__dict__ for course_code, course in self.courses.items()}
        }
        with open(filename, "w") as file:
            json.dump(data, file)
        print("All student and course data saved successfully.")

    def load_data(self, filename="data.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                for student_id, student_data in data["students"].items():
                    student = Student(**student_data)
                    self.students[student_id] = student
                for course_code, course_data in data["courses"].items():
                    course = Course(**course_data)
                    self.courses[course_code] = course
            print("Data loaded successfully.")
        except FileNotFoundError:
            print("No previous data found, starting fresh.")


def main():
    system = StudentManagementSystem()
    system.load_data()

    while True:
        print("\n==== Student Management System ====")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Enroll Student in Course")
        print("4. Add Grade for Student")
        print("5. Display Student Details")
        print("6. Display Course Details")
        print("7. Save Data to File")
        print("8. Load Data from File")
        print("0. Exit")

        option = input("Select Option: ")

        if option == "1":
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            address = input("Enter Address: ")
            student_id = input("Enter Student ID: ")
            system.add_student(name, age, address, student_id)

        elif option == "2":
            course_name = input("Enter Course Name: ")
            course_code = input("Enter Course Code: ")
            instructor = input("Enter Instructor Name: ")
            system.add_course(course_name, course_code, instructor)

        elif option == "3":
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            system.enroll_student_in_course(student_id, course_code)

        elif option == "4":
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            grade = input("Enter Grade: ")
            system.add_grade(student_id, course_code, grade)

        elif option == "5":
            student_id = input("Enter Student ID: ")
            system.display_student_details(student_id)

        elif option == "6":
            course_code = input("Enter Course Code: ")
            system.display_course_details(course_code)

        elif option == "7":
            system.save_data()

        elif option == "8":
            system.load_data()

        elif option == "0":
            print("Exiting Student Management System. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()


