class UnitRecord(object):
    def __init__(self, order: int, chassis: str, engine: str = None):
        self.order = order
        self.chassis = chassis
        self.engine = engine
