from Student import Student


class Grad(Student):
    _thesis = ""

    def __init__(self, name: str, id: int, major: str, thesis: str):
        if isinstance(thesis, str) and thesis is not None:
            super().__init__(name, id, major)
            self._thesis = thesis
            return
        raise Exception("Invalid thesis")

    def update_thesis(self, thesis: str):
        if isinstance(thesis, str) and thesis is not None:
            self._thesis = thesis
            return
        raise Exception("Invalid thesis")

    def __str__(self):
        return super().__str__() + f", {self._thesis}"

        # TESTS


if __name__ == "__main__":
    test_student = Grad
    print(test_student)

    # test_student = Grad("Gradman", 2, "CS", 2022)
    # print(test_student)     # should result in type error for thesis

    test_student = Grad("Gradman", 2, "CS", "Library Management SUStem")
    print("\nShould print Gradman, 2, CS, Library Management SUStem")
    print(test_student)

    test_student.update_major("Amogus")
    print("\nShould print Gradman, 2, Amogus, Library Management SUStem")
    print(test_student)

    test_student.update_thesis("Student Management SUStem")
    print("\nShould print Gradman, 2, Amogus, Student Management SUStem")
    print(test_student)
