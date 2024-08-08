class Student:
    _name = ""
    _id = 0
    _major = ""

    # Sets the attributes if type check passes and vars not empty
    def __init__(self, name: str, id: int, major: str):
        # if name is None or id is None or major is None:
        #     print("Invalid Attributes")
        #     return

        if isinstance(name, str) and not name is None:
            self._name = name
        else:
            raise Exception("Invalid name")
        if isinstance(id, int) and id is not None and id > 0:  # Can do both / 'not' before and in bw
            self._id = id
        else:
            raise Exception("Invalid id")
        if isinstance(major, str) and major is not None:
            self._major = major
        else:
            raise Exception("Invalid major")

        # Changes the major to the input

    def update_major(self, major: str):
        if isinstance(major, str) and major is not None:
            self._major = major
        else:
            raise Exception("Invalid major")

    def __str__(self):
        return f"{self._name}, {self._id}, {self._major}"


    # TESTS


if __name__ == "__main__":
    test_student = Student
    print(test_student)

    # test_student = Student(2, 1, "CS")
    # print(test_student)     # should result in name error

    # test_student = Student("Name", 0, "CS")
    # print(test_student)     # should result in id error

    # test_student = Student("Name", -5, "CS")
    # print(test_student)     # should result in id error   // this results in class... being printed

    # test_student = Student("Name", 2, 2)
    # print(test_student)     # should result in major error

    test_student = Student("Name", 1, "CE")
    print("\nShould print Name, 1, CE")
    print(test_student)

    test_student.update_major("Amogus")
    print("\nShould print Name, 1, Amogus")
    print(test_student)
