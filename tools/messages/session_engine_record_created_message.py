from easter import Message
from tools.models.unit_record import UnitRecord


class SessionEngineRecordCreatedMessage(Message):
    def __init__(self, record: UnitRecord):
        self.record = record
