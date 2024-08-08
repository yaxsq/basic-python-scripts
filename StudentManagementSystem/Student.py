class Student:
    _name = ""
    _id = 0
    major = ""

    def __init__(self, name: str, id: int, major: str):
        self._name = name
        self._id = id
        self.major = major

        # Changes the major to the input
    def update_major(self, new_major: str):
        self.major = new_major

    def __str__(self):
        return f"{self._name}, {self._id}, {self.major}"
