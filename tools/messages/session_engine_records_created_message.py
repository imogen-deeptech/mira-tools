from easter import Message


class SessionEngineRecordsCreatedMessage(Message):
    def __init__(self, engines: list[str]):
        self.engines = engines
