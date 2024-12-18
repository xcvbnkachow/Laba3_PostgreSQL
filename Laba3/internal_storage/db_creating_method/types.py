from dataclasses import dataclass

@dataclass
class MedicalStaff:
    id: int
    surname: str
    address: str
    tax: float


@dataclass
class OperationTypes:
    id: int
    name: str
    strong_point: str
    stocks: int
    cost: float

@dataclass
class WorkActivity:
    contract: int
    weekday: str
    medical_id: int
    jobplace_id: int
    operation_id: int
    amount: int
    payment: float


@dataclass
class JobPlace:
    id: int
    office: str
    address: str
    local_budget_tax: float

