from Student import Student


class Undergrad(Student):
    _year = 0

    def __init__(self, name: str, id: int, major: str, year: int):
        if 2017 < year < 2025:
            super().__init__(name, id, major)
            self._year = year
            return
        raise Exception("Invalid year")

    def update_year(self, year: int):
        if 2017 < year < 2025:
            self._year = year
            return
        raise Exception("Invalid year")

    def __str__(self):
        return super().__str__() + f", {self._year}"

    # TESTS


if __name__ == "__main__":
    test_student = Undergrad
    print(test_student)

    test_student = Undergrad("UG", 1, "CS", 2022)
    print("\nShould print UG, 1, CS, 2022")
    print(test_student)

    test_student.update_details("Amogus")
    print("\nShould print UG, 1, Amogus")
    print(test_student)

    # test_student.update_year(2027)
    # print(test_student)         # should result in invalid year error

    test_student.update_year(2024)
    print(test_student)
