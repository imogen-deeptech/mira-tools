from easter import Message
from tools.models.unit_record import UnitRecord


class SessionChassisRecordCreatedMessage(Message):
    def __init__(self, record: UnitRecord):
        self.record = record
