from Student import Student
from Undergrad import Undergrad
from Grad import Grad
import csv
import atexit

'''
if file exists, open the file and read it
else create a file and continue

menu needs to have add, remove, update info, display all, quit / 5 options

the file will be read and each line will contain one object
the object will be identified by thesis/year using isinstance
a list of Student will be created containing undergrad and grad objects
that local list will then be used to display, modify, etc
before exiting the program, the file will be written to with the updated data

need to fix unique attribute, update, existing file reading error, polymorphism

'''


class Manager:

    def __init__(self):
        self.students = []
        # atexit.register(self._terminate())
        self._read_file()
        self._main()
        self._write_file()

    # reads the file, goes through all lines and uses the list of attributes in a line to get the student object
    # i dont need to create a new file here
    def _read_file(self):
        try:  # trying to open an existing file
            self.file = open("students.csv", "r")
        except FileNotFoundError:  # trying to make a file since it does not exist
            self.file = open("students.csv", "x")
            print("File not found, created a new file")
        else:  # reading from the existing file
            reader = csv.reader(self.file)
            for line in reader:  # populating the students list
                self.students.append(self._create_student_object(line))
            print("Data loaded successfully")
        finally:
            try:
                self.file.close()
            except FileNotFoundError:
                print("No file to close")
            except AttributeError:
                print("No file to close")

    # goes through the students list and writes the attributes to the csv file
    def _write_file(self):
        self.file = open("students.csv", "w")
        for student in self.students:
            csv.writer(self.file).writerow(str(student).split(", "))
        self.file.close()
        print("Data saved successfully")

    # returns the corresponding child class of Student based on the unique attribute (year/thesis)
    @staticmethod
    def _create_student_object(self, line: list) -> Student:
        if isinstance(list[3], int):
            return Undergrad(line[0], line[1], line[2], line[3])
        if isinstance(list[3], str):
            return Grad(line[0], line[1], line[2], line[3])

    # prints data of all students
    def _display_all_students(self):
        for student in self.students:
            if isinstance(student, Undergrad):
                print(f"UG: {student}")
            if isinstance(student, Grad):
                print(f"GR: {student}")

    # adds a new student to the list
    def _add_student(self, name: str, major: str, unique):
        if isinstance(unique, int):  # unique would be year
            self.students.append(Undergrad(name, self._get_new_id(), major, unique))  #
        if isinstance(unique, str):  # unique would be thesis
            self.students.append(Grad(name, self._get_new_id(), major, unique))

    def _get_new_id(self) -> int:
        return len(self.students)+1

    # returns a student object from the students list
    def _get_student(self, name: str, id_number: int) -> Student:
        for student in self.students:
            if student.get_name() == name and student.get_id() == id_number:
                return student
        print("Student not found")

    # returns a student object from the students list using the id only
    def _get_student_using_id(self, id_number: int) -> Student:
        for student in self.students:
            if student.get_id() == id_number:
                return student
        print("Student not found")

    def _delete_student(self, name: str, id_number: int):
        try:
            self.students.remove(self._get_student(name, id_number))
            print(f"{name}, {id} was deleted")
        except ValueError:
            # print("Student not found")        # already printing this in the get function
            return

    # def _update_student_info(self, name: str, id: int, update):
    #     student = self._get_student(name, id)
    #     if isinstance(update, int):  # update would be year
    #
    #
    #     if isinstance(update, str):  # update would be thesis

    def _terminate(self):
        self._write_file()

    def _main(self):
        print("\n*** STUDENT MANAGEMENT SYSTEM ***\n")

        while True:
            print("1. Display all students")
            print("2. Add a new student")
            print("3. Update existing information")
            print("4. Delete a student")
            print("5. Search for a student")
            print("6. Save and Exit")
            choice = int(input("\nEnter your choice (1-5): "))

            if choice == 1:
                self._display_all_students()
            elif choice == 2:
                self._add_student(str(input("Enter name: ")), str(input("Enter major: ")),
                                  eval(input("Enter year/thesis: ")))
            elif choice == 3:
                continue        # yet to implement update
            elif choice == 4:
                self._delete_student(str(input("Enter name: ")), int(input("Enter id: ")))
            elif choice == 5:
                print(self._get_student(str(input("Enter name: ")), int(input("Enter id: "))))
            elif choice == 6:
                break

if __name__ == "__main__":
    sms = Manager()