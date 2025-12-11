from typing import Optional


class CollectRecord(object):
    def __init__(
        self,
        code: str,
        target: str,
        order: int,
        chassis: str,
        engine: Optional[str] = None,
    ):
        self.code = code
        self.target = target
        self.order = order
        self.chassis = chassis
        self.engine = engine

