from easter import Message


class SessionEngineRecordsPopulatedMessage(Message):
    def __init__(self, engines: list[str]):
        self.engines = engines
