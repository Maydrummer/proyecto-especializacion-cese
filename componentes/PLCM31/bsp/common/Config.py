from dataclasses import dataclass

@dataclass
class Config:
    RETRY: int = 3
    TIME_WAIT_EXCEPTION: int = 1
    TIMEOUT_MODBUS: int = 10