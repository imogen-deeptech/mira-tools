from easter import Message


class SessionEntryCreatedMessage(Message):
    def __init__(self, target_id: str, units: list[str]):
        self.target_id = target_id
        self.units = units
