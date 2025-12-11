from typing import Optional


class CollectRecord(object):
    def __init__(
        self,
        code: str,
        target: str,
        order: int,
        chassis: str,
        chassis_status: Optional[str] = None,
        engine: Optional[str] = None,
    ):
        self.code = code
        self.target = target
        self.order = order
        self.chassis = chassis
        self.chassis_status = chassis_status
        self.engine = engine

