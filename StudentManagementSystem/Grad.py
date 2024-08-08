from Student import Student


class Grad(Student):
    _thesis = ""

    def __init__(self, name: str, id: int, major: str, thesis: str):
        if isinstance(thesis, str) and thesis is not None:
            super.__init__(name, id, major)
            self._thesis = thesis
            return
        raise Exception("Invalid thesis")

    def update_thesis(self, thesis: int):
        if isinstance(thesis, str) and thesis is not None:
            self._thesis = thesis
            return
        raise Exception("Invalid thesis")

    def __str__(self):
        return super.__str__() + f" {self._thesis}"
