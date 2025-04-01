from dataclasses import dataclass
from datetime import datetime

@dataclass
class Payment:
    id: int
    payment_type: str
    payment_amount: float
    created: datetime
    status: str
    agent_user_id: int
    device_id: int

@dataclass
class Client:
    device_id: int
    payments: list