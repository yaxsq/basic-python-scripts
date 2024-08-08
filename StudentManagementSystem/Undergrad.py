from Student import Student


class Undergrad(Student):
    _year = 0

    def __init__(self, name: str, id: int, major: str, year: int):
        if 2017 < year < 2025:
            super.__init__(name, id, major)
            self._year = year
            return
        raise Exception("Invalid year")

    def update_year(self, year: int):
        if 2017 < year < 2025:
            self._year = year
            return
        raise Exception("Invalid year")

    def __str__(self):
        return super.__str__() + f" {self._year}"
