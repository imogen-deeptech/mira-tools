from easter import Message


class SessionEntryCreatedMessage(Message):
    def __init__(self, code: str, target: str, units: list[str]):
        self.code = code
        self.target = target
        self.units = units

    class Builder:
        def __init__(self):
            self.code = None
            self.target = None
            self.units = []

        def with_code(self, code: str):
            self.code = code
            return self

        def with_target(self, target: str):
            self.target = target
            return self

        def with_units(self, units: list[str]):
            self.units = units
            return self

        def add_unit(self, unit: str):
            self.units.append(unit)
            return self

        def build(self):
            if self.code is None or self.target is None:
                raise ValueError("Code and target must be set")
            return SessionEntryCreatedMessage(self.code, self.target, self.units)
