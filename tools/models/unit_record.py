from typing import Optional


class UnitRecord(object):
    def __init__(self, order: int, chassis: str, engine: Optional[str] = None):
        self.order = order
        self.chassis = chassis
        self.engine = engine
