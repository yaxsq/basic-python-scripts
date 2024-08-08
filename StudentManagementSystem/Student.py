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
        if isinstance(id, int) and id is not None:      # Can do both / 'not' before and in bw
            self._id = id
        if isinstance(major, str) and major is not None:
            self.major = major

        # Changes the major to the input
    def update_major(self, major: str):
        if isinstance(major, str) and major is not None:
            self.major = major

    def __str__(self):
        return f"{self._name}, {self._id}, {self.major}"
