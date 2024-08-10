from Student import Student
from Undergrad import Undergrad
from Grad import Grad
import csv
import atexit

'''
RUN THIS FILE FOR CLI

if file exists, open the file and read it
~else create a file and continue~

menu needs to have add, remove, update info, display all, quit / 5 options

the file will be read and each line will contain one object
the object will be identified by thesis/year using isinstance
a list of Student will be created containing undergrad and grad objects
that local list will then be used to display, modify, etc
before exiting the program, the file will be overwritten to with the updated data

need to fix unique attribute, ~update~, ~existing file reading error~

string reading caused the file reading error
the create student method caused the error
it was fixed by converting the unique attribute to its type before passing to the constructor

the update problem was due to the student object not being declared explicitly
that cant be done so isinstance was used to identify the object type
the subclass method was then used along with identifying the input type to determine the subclass type

the idea of method overriding to update data was scrapped 
separate methods were created to update the major, year and thesis

'''


class Manager:

    def __init__(self):
        self.students = []
        # atexit.register(self._terminate())
        self._read_file()
        # self.cli()
        # self._write_file()

    # reads the file, goes through all lines and uses the list of attributes in a line to get the student object
    # i dont need to create a new file here
    def _read_file(self):
        try:  # trying to open an existing file
            self.file = open("students.csv", "r")
        except FileNotFoundError:  # trying to make a file since it does not exist
            # self.file = open("students.csv", "x")
            print("File not found, created a new file")
        else:  # reading from the existing file
            reader = csv.reader(self.file)
            for line in reader:  # populating the students list
                print(f"Line: {line}")
                self.students.append(self._create_student_object(line))
                print(f"List: {self.students}")
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
            if student is not None:
                csv.writer(self.file).writerow(str(student).split(", "))
        self.file.close()
        print("Data saved successfully")

    # returns the corresponding child class of Student based on the unique attribute (year/thesis)
    @staticmethod
    def _create_student_object(line: list) -> Student:
        if not len(line) == 0:
            try:
                unique = int(line[3])
            except ValueError:
                return Grad(line[0], line[1], line[2], line[3])
            else:
                return Undergrad(line[0], line[1], line[2], unique)

        # if isinstance(list[3], int):
        #     return Undergrad(line[0], line[1], line[2], line[3])
        # if isinstance(list[3], str):
        #     return Grad(line[0], line[1], line[2], line[3])

    # prints data of all students
    def _display_all_students(self):
        for student in self.students:
            if isinstance(student, Undergrad):
                print(f"UG: {student}")
            if isinstance(student, Grad):
                print(f"GR: {student}")
            if student is None:
                continue
        print()

    # adds a new student to the list
    def _add_student(self, name: str, major: str, unique):
        if isinstance(unique, int):  # unique would be year
            self.students.append(Undergrad(name, self._get_new_id(), major, unique))  #
        if isinstance(unique, str):  # unique would be thesis
            self.students.append(Grad(name, self._get_new_id(), major, unique))

    def _get_new_id(self) -> int:
        return len(self.students) + 1

    # returns a student object from the students list
    def _get_student(self, name: str, id_number: int) -> Student:
        for student in self.students:
            if student is not None and student.get_name() == name and student.get_id() == id_number:
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

    # updates the major of the student
    def _update_student_major(self, student: Student, major: str):
        if isinstance(major, str):
            student.update_major(major)
        else:
            print("Invalid major type")

    # specifically updates the year/thesis of the student
    def _update_student_unique_attribute(self, student: Student, unique):
        if isinstance(student, Undergrad):
            try:
                unique = int(unique)
            except ValueError:
                print("Invalid year type")
            else:
                student.update_year(unique)
        elif isinstance(student, Grad):
            if isinstance(unique, str):
                student.update_thesis(unique)
            else:
                print("Invalid thesis type")

    def _update_student_info(self, name: str, id_number: int):
        choice = int(input("Would you like to update the major(1) or year/thesis(2)? (1-2): "))
        update = input("Enter the new information: ")
        student = self._get_student(name, id_number)

        if choice == 1:
            self._update_student_major(student, update)
        elif choice == 2:
            self._update_student_unique_attribute(student, update)

    def _terminate(self):
        self._write_file()

    def cli(self):
        print("\n*** STUDENT MANAGEMENT SYSTEM ***\n")

        while True:
            print("1. Display all students")
            print("2. Add a new student")
            print("3. Update existing information")
            print("4. Delete a student")
            print("5. Search for a student")
            print("6. Save and Exit")
            try:
                choice = int(input("\nEnter your choice (1-5): "))
            except ValueError:
                print("Invalid choice, try again")
                continue

            if choice == 1:
                self._display_all_students()
            elif choice == 2:
                # self._add_student(str(input("Enter name: ")), str(input("Enter major: ")),
                #                   eval(input("Enter year/thesis: ")))
                name = str(input("Enter name: "))
                major = str(input("Enter major: "))
                unique = input("Enter year/thesis: ")
                try:
                    unique = int(unique)
                except ValueError:  # passes string to add student, meaning the student is grad type
                    self._add_student(name, major, unique)
                else:  # passes int to add student, meaning student is of undergrad type
                    self._add_student(name, major, unique)
            elif choice == 3:
                self._update_student_info(input("Enter name: "), int(input("Enter id: ")))
            elif choice == 4:
                self._delete_student(str(input("Enter name: ")), int(input("Enter id: ")))
            elif choice == 5:
                print(self._get_student(str(input("Enter name: ")), int(input("Enter id: "))))
            elif choice == 6:
                self._write_file()
                break


if __name__ == "__main__":
    sms = Manager()
    sms.cli()

# SAMPLE DATA
# amog, 1, 1, 2020
#
# amog3, 5, compsci, sussy
#
# amog5, 7, civileng, 2023
#
