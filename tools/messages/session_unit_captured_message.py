from easter import Message
from tools.models.unit_record import UnitRecord


class SessionEntryCreatedMessage(Message):
    def __init__(self, code: str, target: str, unit: UnitRecord):
        self.code = code
        self.target = target
        self.unit = unit

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

        def with_unit(self, unit: UnitRecord):
            self.unit = unit
            return self

        def build(self):
            if self.code is None or self.target is None or self.unit is None:
                raise ValueError("Code, target, and unit must be set")
            return SessionEntryCreatedMessage(self.code, self.target, self.unit)