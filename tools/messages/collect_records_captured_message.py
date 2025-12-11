from easter import Message
from tools.models.collect_record import CollectRecord


class CollectRecordsCapturedMessage(Message):
    def __init__(self, records: list[CollectRecord]):
        self.records = records
